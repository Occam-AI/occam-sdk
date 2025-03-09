import requests
import logging

from enum import Enum
from typing import Tuple

from functools import wraps
from requests import Response


# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class AgentAction(Enum):
    PAUSE = "pause"
    RESUME = "resume"
    TERMINATE = "terminate"


def authenticate_with_occam_api(base_url: str, api_key: str) -> Tuple[str, int]:
    """
    Perform auth using the provided API key.
    Raises an exception if the key is invalid.
    """
    # The auth endpoint (GET /auth/access-token?key=...)
    url = f"{base_url}/auth/access-token"
    params = {"key": api_key}
    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        raise ValueError(
            f"Authentication failed. Check API key. "
            f"Status code: {response.status_code}. "
            f"Details: {response.text}"
        )

    data = response.json()
    access_token = data["access_token"]
    expires_at = data.get("expires_at")  # In case you want to handle token exp later
    return access_token, expires_at


def retry_once_on_unauthorized(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except requests.exceptions.HTTPError as e:
            response: Response = e.response
            if response.status_code == 401:
                logger.info("Received 401, attempting re-authentication to generate a new access token")
                # Re-authenticate and update the access token
                self._access_token, self._expires_at = authenticate_with_occam_api(
                    base_url=self._base_url,
                    api_key=self._api_key
                )
                # Retry the original request with new token
                return func(self, *args, **kwargs)
            raise  # Re-raise if it's not a 401
    return wrapper
