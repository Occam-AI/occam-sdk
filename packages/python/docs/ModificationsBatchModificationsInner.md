# ModificationsBatchModificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role_description** | **str** |  | 
**node_id** | **int** |  | 
**plan_id** | **str** |  | 
**params** | **Dict[str, object]** |  | [optional] 
**adapter_query** | [**AdapterQuery**](AdapterQuery.md) |  | [optional] 
**type** | **object** |  | [optional] 
**data_source_access_name** | **str** |  | [optional] 
**is_proposed** | **bool** |  | [optional] [default to False]
**src_type** | [**PlanElementType**](PlanElementType.md) |  | 
**src** | **int** |  | 
**target** | **int** |  | 
**src_output_field** | **str** |  | 
**target_input_field** | **str** |  | 

## Example

```python
from occam_sdk.models.modifications_batch_modifications_inner import ModificationsBatchModificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModificationsBatchModificationsInner from a JSON string
modifications_batch_modifications_inner_instance = ModificationsBatchModificationsInner.from_json(json)
# print the JSON string representation of the object
print(ModificationsBatchModificationsInner.to_json())

# convert the object into a dict
modifications_batch_modifications_inner_dict = modifications_batch_modifications_inner_instance.to_dict()
# create an instance of ModificationsBatchModificationsInner from a dict
modifications_batch_modifications_inner_from_dict = ModificationsBatchModificationsInner.from_dict(modifications_batch_modifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


