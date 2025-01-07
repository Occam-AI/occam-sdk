# AddFieldMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_type** | [**PlanElementType**](PlanElementType.md) |  | 
**src** | **int** |  | 
**target** | **int** |  | 
**src_output_field** | **str** |  | 
**target_input_field** | **str** |  | 
**plan_id** | **str** |  | 
**type** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.add_field_mapping import AddFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AddFieldMapping from a JSON string
add_field_mapping_instance = AddFieldMapping.from_json(json)
# print the JSON string representation of the object
print(AddFieldMapping.to_json())

# convert the object into a dict
add_field_mapping_dict = add_field_mapping_instance.to_dict()
# create an instance of AddFieldMapping from a dict
add_field_mapping_from_dict = AddFieldMapping.from_dict(add_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


