
import os
from typing import Dict

from occam_core.agents.model import AgentIOModel, AgentIdentityCoreModel
from occam_core.model_catalogue import PARAMS_MODEL_CATALOGUE
from occam_core.util.base_models import ParamsIOModel
from occam_sdk.api_client import OccamClient


def _select_agent(catalogue: Dict[str, AgentIdentityCoreModel]) -> str:
    # Select agent based on some criteria
    return "openai/o1"


if __name__ == "__main__":
    api_key = os.getenv("OCCAM_API_KEY")
    base_url = os.getenv("OCCAM_BASE_URL", "http://127.0.0.1:8000")
    # In your application or tests:
    client = OccamClient(api_key=api_key, base_url=base_url)

    # List agents
    agents_catalogue = client.agents.get_agents_catalogue()
    print("List of agents below:")
    for agent_name in agents_catalogue.keys():
        print(agent_name)
    
    print("==================")

    # Select agent based on some criteria
    agent_name = _select_agent(agents_catalogue)

    # Get a specific agent
    some_agent = client.agents.get_agent(agent_name=agent_name)
    partial_params = some_agent.partial_params
    params_model = PARAMS_MODEL_CATALOGUE[some_agent.params_model_name]

    # Create a new agent instance
    agent_instantiation_response = client.agents.instantiate_agent(
        agent_name=agent_name,
        agent_params_model=params_model(
            **partial_params.model_dump(),
        )
    )
    agent_instance_id = list(agent_instantiation_response.keys())[0]
    agent_identity = list(agent_instantiation_response.values())[0]
    print(f"Created agent:")
    print(f"Agent instance ID: {agent_instance_id}")
    print(f"Agent identity: {agent_identity}")

    print("==================")

    # Run the agent
    agent_run = client.agents.run_agent(
        agent_instance_id=agent_instance_id,
        agent_input_model=AgentIOModel(
            query="What is the weather in Tokyo?",
        )
    )

    # Check status
    run_status = client.agents.get_agent_run_status(agent_run.agent_run_instance_id)
    print(f"Run status: {run_status}")
    print("==================")
    # Get run result
    run_result = client.agents.get_agent_run_result(agent_run.agent_run_instance_id)

    print("Run result:")
    print(run_result)
