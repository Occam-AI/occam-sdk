# Using the Occam Agents API

This document explains how to use the Agents API provided by the Occam SDK. These
endpoints allow you to:

1. Browse available agents via a catalogue.
2. Inspect specific agent metadata.
3. Instantiate agents by providing the proper parameters.
4. Run those agents (with input messages or data).
5. Manage long-running jobs (pause, resume, or terminate).
6. Track running agents and retrieve their run results.


---

## Key Concepts

- **Agents**: Agents are specialized entities that operate on agent I/O data.
These agents can be humans, to be leveraged through Occam's Agents Chat Tool,
or AI based agents, such as a web-browser, a data querying agent or an email
communicator. All agents have the same base IO structure of queries or chat messages
but can also accept additional custom inputs if needed. They can be run, paused,
resumed, terminated, and some can be communicated within in real-time where a
dashboard is to be present for them.

- **AgentIdentityCoreModel**: Defines properties for each agent, such as
  description, contact info, or requirements.
- **ParamsIOModel**: Used when creating new agent instances. Each agent's
  `AgentIdentityCoreModel` references the `params_model_name` indicating which
  parameter schema to use.
- **AgentIOModel**: The structure for input to an agent, commonly a list of
  messages (similar to an OpenAI chat format).

---

## Endpoints Overview

Below is a summary of the most important endpoints in the `AgentsApi` class.


1. **get_agents_catalogue**
   • Fetches a catalogue of agents accessible to you.
   • Returns a dictionary keyed by agent name, each value containing an
     `AgentIdentityCoreModel` with descriptive info, contact data, and other
     metadata.

2. **get_agent_metadata**
   • Retrieves metadata (`AgentIdentityCoreModel`) for a single agent.
   • Can also return an `AgentHandlingError` if something goes wrong.

3. **instantiate_agent**
   • Creates an instance of an agent using a `ParamsIOModel` that matches the
     agent's `params_model_name`.
   • Returns `AgentInstanceMetadata` or an `AgentHandlingError`.

4. **run_agent**
   • Runs the agent instance created via `instantiate_agent`.
   • Requires an `AgentIOModel` (often representing messages).
   • Returns an `AgentRunDetail` or an `AgentHandlingError`.
   • Optionally runs synchronously (`sync=True`) or asynchronously.

5. **get_agent_run_detail**
   • Retrieves the current status of a run, including final results.
   • Returns `AgentRunDetail` or an `AgentHandlingError`.

6. **manage_agent**
   • Allows pausing (`PAUSE`), resuming (`RESUME`), or terminating (`TERMINATE`)
     agent runs.
   • Returns an updated `AgentRunDetail` or an `AgentHandlingError`.

7. **list_running_agents**
   • Returns all currently running agents' `AgentRunDetail`.

---

## Example Usage

You can see an example script in
[src/python/scripts/example_run_agent.py](src/python/scripts/example_run_agent.py).

Below is a simplified flow:

```python
import os
import time
from occamai.api_client import OccamClient
from occam_core.util.base_models import ParamsIOModel
from occam_core.agents.model import AgentIOModel
from occam_core.model_catalogue import PARAMS_MODEL_CATALOGUE


def run_agent_example():
    # Set up client (replace with correct key & URL)
    client = OccamClient(
        base_url="https://api.occam.ai",
        api_key="YOUR_API_KEY"
    )

    # 1. List agents
    catalogue = client.agents.get_agents_catalogue()
    print("Available agents:", catalogue.keys())

    # 2. Retrieve specific agent metadata
    agent_name = "ExampleAgent"
    agent_meta = client.agents.get_agent_metadata(agent_name)
    print("Agent metadata:", agent_meta)

    params_model = PARAMS_MODEL_CATALOGUE[agent_meta.params_model_name]

    # 3. Instantiate agent
    agent_params = params_model(param1="value1", param2="value2")
    instance_data = client.agents.instantiate_agent(
        agent_name,
        agent_params
    )

    # 4. Run agent
    agent_input = AgentIOModel(
        chat_messages=[{"role": "user", "content": "Hello!"}]
    )
    run_detail = client.agents.run_agent(
        instance_data.instance_id,
        agent_input,
        sync=True
    )
    print("Run detail:", run_detail)

    # 5. Manage or track run status if needed
    # (Pause, Resume, or Terminate)
    timeline = client.agents.manage_agent(
        instance_data.instance_id,
        AgentAction.PAUSE,
        sync=True
    )
    print("Timeline:", timeline)

    # 6. Check final status
    final_status = client.agents.get_agent_run_detail(
        instance_data.instance_id
    )
    print("Final status:", final_status)
```

In your real projects, you'll potentially add error handling for each step,
checking for an `AgentHandlingError` before proceeding.

---

## Human Agents

(e.g., can they upload files, read, write, or end the chat?). The relevant
parameters are provided in the `ParamsIOModel` specific to that human agent.
sure you specify their permissions in the Occam Human-In-The-Loop environment
(e.g., whether they can upload files, have read/write access, or end the chat).

---

By following these steps, you can integrate Occam's Agents API into your
applications. For more details, consult the docstrings in `api_client.py` and
review the provided example script.
