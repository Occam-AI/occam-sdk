
import os

from occam_core.agents.model import AgentIOModel
from occam_core.util.base_models import ParamsIOModel
from occam_sdk.api_client import OccamClient

if __name__ == "__main__":
    api_key = os.getenv("OCCAM_API_KEY")
    base_url = os.getenv("OCCAM_BASE_URL", "http://127.0.0.1:8000")
    # In your application or tests:
    client = OccamClient(api_key=api_key, base_url=base_url)

    # List agents
    agents_catalogue = client.agents.get_agents_catalogue()
    for agent in agents_catalogue:
        print(f"Agent: {agent}")
        print("======")

    # Get a specific agent
    some_agent = client.agents.get_agent(agent_name="WebBrowsingLlmTool")
    # params_model = MODEL_CATALOGUE[some_agent.params_model_name]

    # Create a new agent instance
    agent_instantiation_response = client.agents.instantiate_agent(
        agent_name="WebBrowsingLlmTool",
        agent_params_model=ParamsIOModel(
            param1="value1",
            # ...
        )
    )
    print(f"Created agent: {agent_instantiation_response.response_model.agent_instance_id}")

    # Run the agent
    agent_run = client.agents.run_agent(
        agent_instance_id=agent_instantiation_response.response_model.agent_instance_id,
        agent_input_model=AgentIOModel(
            query="What is the weather in Tokyo?",
        )
    )

    # Check status
    run_status = client.agents.get_agent_run_status(agent_instantiation_response.agent_instance_id)
    # Get run result
    run_result = client.agents.get_agent_run_result(agent_instantiation_response.agent_instance_id)
    print(run_status)
    print(run_result)
