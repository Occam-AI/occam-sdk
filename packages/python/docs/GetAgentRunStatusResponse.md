# GetAgentRunStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AgentRunStatus**](AgentRunStatus.md) |  | 

## Example

```python
from occam_sdk.models.get_agent_run_status_response import GetAgentRunStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentRunStatusResponse from a JSON string
get_agent_run_status_response_instance = GetAgentRunStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetAgentRunStatusResponse.to_json())

# convert the object into a dict
get_agent_run_status_response_dict = get_agent_run_status_response_instance.to_dict()
# create an instance of GetAgentRunStatusResponse from a dict
get_agent_run_status_response_from_dict = GetAgentRunStatusResponse.from_dict(get_agent_run_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


