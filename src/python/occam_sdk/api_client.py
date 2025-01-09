from typing import Any, Dict, Optional

import requests
from urllib.parse import quote
from occam_core.agents.model import AgentIdentityCoreModel, AgentIOModel
from occam_core.api_util import (AgentInstanceMetadata, AgentRunDetail,
                                 AgentSetupError)
from occam_core.util.base_models import ParamsIOModel

from occam_sdk.util import (AgentFetchError, AgentInstanceFetchError, AgentInstanceMetadata,
                            AgentInstantiationError, AgentRunDetail)


class AgentsApi:
    """
    Simple wrapper for the /agents/ endpoints.
    """

    def __init__(self, base_url: str, access_token: str):
        self._base_url = base_url
        self._access_token = access_token

    def _headers(self) -> Dict[str, str]:
        """
        Return common headers, including auth.
        """
        return {
            "Authorization": f"Bearer {self._access_token}",
            "Content-Type": "application/json",
        }

    def get_agents_catalogue(self) -> Dict[str, AgentIdentityCoreModel]:
        """
        Corresponds to GET /agents
        Returns a list of agents available to the current user.
        """
        url = f"{self._base_url}/agents"
        resp = requests.get(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        agent_catalogue_dict = resp.json()
        return {agent_name: AgentIdentityCoreModel.model_validate(agent_dict)
                for agent_name, agent_dict in agent_catalogue_dict.items()}

    def get_agent(self, agent_name: str) -> AgentIdentityCoreModel | AgentSetupError:
        """
        Corresponds to GET /agents/{agent_name}
        Returns the metadata of the specified agent.
        """
        # Agent name might include "/" or other special characters that would mess up the URL
        encoded_agent_name = quote(agent_name, safe='')
        url = f"{self._base_url}/agents/{encoded_agent_name}"
        resp = requests.get(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        identity_dict = resp.json()
        if "error_message" in identity_dict:
            return AgentSetupError.model_validate(identity_dict)
        return AgentIdentityCoreModel.model_validate(identity_dict)

    def instantiate_agent(self, agent_name: str, agent_params: ParamsIOModel) -> AgentInstanceMetadata | AgentSetupError:
        """
        Corresponds to POST /agents/{agent_name}/create
        Creates an instance of an agent.
        """
        if not isinstance(agent_params_model, ParamsIOModel):
            raise ValueError("agent_params_model must be an instance of ParamsIOModel")
        encoded_name = quote(agent_name, safe='')
        url = f"{self._base_url}/agents/{encoded_name}/instantiate"
        agent_params = agent_params_model.model_dump()
        resp = requests.post(url, headers=self._headers(), json=agent_params, timeout=10)
        resp.raise_for_status()
        response_dict = resp.json()
        if "error_type" in response_dict:
            return AgentSetupError.model_validate(response_dict)
        return AgentInstanceMetadata.model_validate(response_dict)

    def run_agent(self, agent_instance_id: str, agent_input_model: AgentIOModel) -> AgentRunDetail | AgentSetupError:
        """
        Corresponds to POST /agents/{agent_instance_id}/run
        Runs the specified agent instance with provided input.
        """
        if not isinstance(agent_input_model, AgentIOModel):
            raise ValueError("agent_input_model must be an instance of AgentIOModel")
        url = f"{self._base_url}/agents/{agent_instance_id}/run"
        agent_input = {"inputs": agent_input_model.model_dump()}
        resp = requests.post(url, headers=self._headers(), json=agent_input, timeout=10)
        resp.raise_for_status()
        response_dict = resp.json()
        if "error_type" in response_dict:
            return AgentSetupError.model_validate(response_dict)
        return AgentRunDetail.model_validate(response_dict)

    def get_agent_run_status(self, agent_run_instance_id: str) -> AgentRunDetail | AgentSetupError:
        """
        Corresponds to GET /agents/run/{agent_run_instance_id}/status
        Returns the status of the specified agent run.
        """
        url = f"{self._base_url}/agents/{agent_run_instance_id}/run/status"
        resp = requests.post(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        response_dict = resp.json()
        if "error_type" in response_dict:
            return AgentInstanceFetchError.model_validate(response_dict)
        response_dict["agent_run_instance_id"] = agent_run_instance_id
        return AgentRunDetail.model_validate(response_dict)

    def get_agent_run_result(self, agent_run_instance_id: str) -> AgentIOModel | AgentSetupError:
        """
        Corresponds to GET /agents/run/{agent_run_instance_id}/result
        Returns the results of the specified agent run.
        """
        url = f"{self._base_url}/agents/{agent_run_instance_id}/run/result"
        resp = requests.post(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()

        response_dict = resp.json()
        if "error_type" in response_dict:
            return AgentSetupError.model_validate(response_dict)
        return AgentIOModel.model_validate(response_dict)


class OccamClient:
    """
    OccamClient provides a simple interface for authenticating with
    the Occam API and calling agent endpoints.
    """

    def __init__(
        self,
        base_url: str = "https://api.occam.ai",
        api_key: str = ""
    ):
        """
        :param base_url: Base URL for the Occam API (defaults to https://api.occam.ai)
        :param api_key: Your API key for Occam
        """
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._access_token: Optional[str] = None
        self._expires_at: Optional[int] = None
        self._agents_api: Optional["AgentsApi"] = None

        # Attempt authentication immediately so we fail fast if invalid
        self._authenticate()

    def _authenticate(self) -> None:
        """
        Perform auth using the provided API key.
        Raises an exception if the key is invalid.
        """
        # The auth endpoint (GET /auth/access-token?key=...)
        url = f"{self._base_url}/auth/access-token"
        params = {"key": self._api_key}
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            raise ValueError(
                f"Authentication failed. Check API key. "
                f"Status code: {response.status_code}. "
                f"Details: {response.text}"
            )

        data = response.json()
        self._access_token = data["access_token"]
        self._expires_at = data.get("expires_at")  # In case you want to handle token exp later

    @property
    def agents(self) -> AgentsApi:
        """
        Access the Agents endpoints. For example:
            client.agents.get_agents()
            client.agents.get_agent("SomeAgent")
            client.agents.instantiate_agent(agent_name="SomeAgent", agent_params={...})
            client.agents.run_agent(agent_instance_id="xxxx", agent_input_model={...})
            client.agents.get_agent_run_status("xxxx")
            client.agents.get_agent_run_result("xxxx")
        """
        if self._agents_api is None:
            self._agents_api = AgentsApi(base_url=self._base_url, access_token=self._access_token)
        return self._agents_api
