
from occam_sdk.api_client import OccamClient


if __name__ == "__main__":
    # In your application or tests:
    client = OccamClient(api_key="sk-occam-d75ed2b8153b4a3ba1c1a08012899551", base_url="http://127.0.0.1:8000")

    # List agents
    agents_list = client.agents.list_agents()

    # Get a specific agent
    some_agent = client.agents.get_agent(agent_name="WebBrowsingLlmTool")

    # Create a new agent instance
    created_agent = client.agents.create_agent(
        agent_name="WebBrowsingLlmTool",
        request_body={
            "param1": "value1",
            # ...
        }
    )

    # Run the agent
    agent_run = client.agents.run_agent(
        agent_instance_id=created_agent["agent_instance_id"],
        request_body={
            "inputs": [
                {
                    "input1": "value1",
                },
                {
                    "input2": "value2",
                },
            ]
        }
    )

    # Check status
    run_status = client.agents.get_agent_run_status(agent_run["agent_run_instance_id"])
    run_result = client.agents.get_agent_run_result(agent_run["agent_run_instance_id"])
    print(run_status)
    print(run_result)
