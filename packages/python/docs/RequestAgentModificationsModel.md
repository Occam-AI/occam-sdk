# RequestAgentModificationsModel

This is the model that is sent to the planner to request feedback including incorporating user modifications, validating them then making suggestions for changes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifications_batch** | [**ModificationsBatch**](ModificationsBatch.md) |  | [optional] 
**user_message** | [**UserMessageModel**](UserMessageModel.md) |  | [optional] 

## Example

```python
from occam_sdk.models.request_agent_modifications_model import RequestAgentModificationsModel

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAgentModificationsModel from a JSON string
request_agent_modifications_model_instance = RequestAgentModificationsModel.from_json(json)
# print the JSON string representation of the object
print(RequestAgentModificationsModel.to_json())

# convert the object into a dict
request_agent_modifications_model_dict = request_agent_modifications_model_instance.to_dict()
# create an instance of RequestAgentModificationsModel from a dict
request_agent_modifications_model_from_dict = RequestAgentModificationsModel.from_dict(request_agent_modifications_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


