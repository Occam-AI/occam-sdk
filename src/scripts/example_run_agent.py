
import os
from occam_sdk.api_client import OccamClient

from occam_core.base_models import ParamsIOModel
from occam_core.agents.model import AgentIOModel


if __name__ == "__main__":
    api_key = os.getenv("OCCAM_API_KEY")
    base_url = os.getenv("OCCAM_BASE_URL", "http://127.0.0.1:8000")
    # In your application or tests:
    client = OccamClient(api_key=api_key, base_url=base_url)

    # List agents
    agents_list = client.agents.list_agents()
    for agent in agents_list:
        print(f"Agent: {agent}")
        print("======")

    # Get a specific agent
    some_agent = client.agents.get_agent(agent_name="WebBrowsingLlmTool")
    # params_model = MODEL_CATALOGUE[some_agent.params_model_name]

    # Create a new agent instance
    created_agent = client.agents.instantiate_agent(
        agent_name="WebBrowsingLlmTool",
        agent_params_model=ParamsIOModel(
            param1="value1",
            # ...
        )
    )
    print(f"Created agent: {created_agent}")

    # Run the agent
    agent_run = client.agents.run_agent(
        agent_instance_id=created_agent["agent_instance_id"],
        request_body={
            "inputs": [
                AgentIOModel(
                    input1="value1",
                ),
                AgentIOModel(
                    input2="value2",
                ),
            ]
        }
    )

    # Check status
    run_status = client.agents.get_agent_run_status(agent_run["agent_run_instance_id"])
    # Get run result
    run_result = client.agents.get_agent_run_result(agent_run["agent_run_instance_id"])
    print(run_status)
    print(run_result)
