
import os
import time
from typing import Dict

from occam_core.agents.model import AgentIdentityCoreModel, AgentIOModel
from occam_core.api_util import AgentRunStatus
from occam_core.model_catalogue import PARAMS_MODEL_CATALOGUE
from occamai.api_client import OccamClient


def _select_agent(catalogue: Dict[str, AgentIdentityCoreModel]) -> str:
    # Select agent based on some criteria
    return "openai/o1"


# NOTES: TODO: Mo/Ahmed

# 1. support streaming


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
    some_agent = client.agents.get_agent_metadata(agent_name=agent_name)
    params_model = PARAMS_MODEL_CATALOGUE[some_agent.params_model_name]

    agent_params  = params_model(
        system_prompt="You are a helpful assistant.",
        assistant_name="Assistant",
    )

    # Create a new agent instance
    agent_instantiation_response = client.agents.instantiate_agent(
        agent_name=agent_name,
        agent_params=agent_params
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
        ),
        sync=False
    )

    # Check status
    run_status = client.agents.get_agent_run_detail(agent_run.agent_run_instance_id)
    print(f"Run status: {run_status}")
    print("==================")

    while run_status.status != AgentRunStatus.COMPLETED:
        time.sleep(1)
        run_status = client.agents.get_agent_run_detail(agent_run.agent_run_instance_id)
        print(f"Run status: {run_status}")

    print("Run result:")
    print(run_status.result)
