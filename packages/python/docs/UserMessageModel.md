# UserMessageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**nodes** | **List[int]** |  | [optional] 
**field_mappings** | [**List[PlanFieldMapping]**](PlanFieldMapping.md) |  | [optional] 

## Example

```python
from occam_sdk.models.user_message_model import UserMessageModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserMessageModel from a JSON string
user_message_model_instance = UserMessageModel.from_json(json)
# print the JSON string representation of the object
print(UserMessageModel.to_json())

# convert the object into a dict
user_message_model_dict = user_message_model_instance.to_dict()
# create an instance of UserMessageModel from a dict
user_message_model_from_dict = UserMessageModel.from_dict(user_message_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


