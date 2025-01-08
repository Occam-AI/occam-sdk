import requests
from typing import Optional, Dict, Any
from occam_core.base_models import ParamsIOModel
from occam_core.agents.model import AgentIOModel, AgentIdentityCoreModel 


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
    def agents(self) -> "AgentsApi":
        """
        Access the Agents endpoints. For example:
            client.agents.list_agents()
            client.agents.get_agent("SomeAgent")
            client.agents.create_agent(agent_name="SomeAgent", request_body={...})
            client.agents.run_agent(agent_instance_id="xxxx", request_body={...})
            client.agents.get_agent_run_status("xxxx")
        """
        if self._agents_api is None:
            self._agents_api = AgentsApi(base_url=self._base_url, access_token=self._access_token)
        return self._agents_api


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

    def get_agent(self, agent_name: str) -> AgentIdentityCoreModel:
        """
        Corresponds to GET /agents/{agent_name}
        Returns the metadata of the specified agent.
        """
        url = f"{self._base_url}/agents/{agent_name}"
        resp = requests.get(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        identity_dict = resp.json()
        return AgentIdentityCoreModel.model_validate(identity_dict)

    def instantiate_agent(self, agent_name: str, agent_params_model: ParamsIOModel) -> AgentIdentityCoreModel:
        """
        Corresponds to POST /agents/{agent_name}/create
        Creates an instance of an agent.
        """
        url = f"{self._base_url}/agents/{agent_name}/instantiate"
        agent_params = agent_params_model.model_dump()
        resp = requests.post(url, headers=self._headers(), json=agent_params, timeout=10)
        resp.raise_for_status()
        return AgentIdentityCoreModel.model_validate(resp.json())

    def run_agent(self, agent_instance_id: str, agent_input_model: AgentIOModel) -> Dict[str, Any]:
        """
        Corresponds to POST /agents/{agent_instance_id}/run
        Runs the specified agent instance with provided input.
        """
        url = f"{self._base_url}/agents/{agent_instance_id}/run"
        agent_input = agent_input_model.model_dump()
        resp = requests.post(url, headers=self._headers(), json=agent_input, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def get_agent_run_status(self, agent_run_instance_id: str) -> Dict[str, Any]:
        """
        Corresponds to GET /agents/{agent_run_instance_id}/status
        Returns the status of the specified agent run.
        """
        url = f"{self._base_url}/agents/run/{agent_run_instance_id}/status"
        resp = requests.get(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        return resp.json()

    def get_agent_run_result(self, agent_run_instance_id: str) -> AgentIOModel:
        """
        Corresponds to GET /agents/{agent_run_instance_id}/result
        Returns the results of the specified agent run.
        """
        url = f"{self._base_url}/agents/run/{agent_run_instance_id}/result"
        resp = requests.get(url, headers=self._headers(), timeout=10)
        resp.raise_for_status()

        output_dict = resp.json()
        return AgentIOModel.model_validate(output_dict)
