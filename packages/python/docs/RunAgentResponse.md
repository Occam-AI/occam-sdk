# RunAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_run_instance_id** | **str** |  | 

## Example

```python
from occam_sdk.models.run_agent_response import RunAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunAgentResponse from a JSON string
run_agent_response_instance = RunAgentResponse.from_json(json)
# print the JSON string representation of the object
print(RunAgentResponse.to_json())

# convert the object into a dict
run_agent_response_dict = run_agent_response_instance.to_dict()
# create an instance of RunAgentResponse from a dict
run_agent_response_from_dict = RunAgentResponse.from_dict(run_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


