# ModificationsBatch

This is the model that is expected by the save and validate endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifications** | [**List[ModificationsBatchModificationsInner]**](ModificationsBatchModificationsInner.md) |  | 
**modifier_id** | **int** |  | [optional] 
**modifier_type** | [**PlanModifierType**](PlanModifierType.md) |  | 

## Example

```python
from occam_sdk.models.modifications_batch import ModificationsBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ModificationsBatch from a JSON string
modifications_batch_instance = ModificationsBatch.from_json(json)
# print the JSON string representation of the object
print(ModificationsBatch.to_json())

# convert the object into a dict
modifications_batch_dict = modifications_batch_instance.to_dict()
# create an instance of ModificationsBatch from a dict
modifications_batch_from_dict = ModificationsBatch.from_dict(modifications_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


