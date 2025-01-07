# EditNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**node_id** | **int** |  | 
**params** | **Dict[str, object]** |  | [optional] 
**adapter_query** | [**AdapterQuery**](AdapterQuery.md) |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.edit_node import EditNode

# TODO update the JSON string below
json = "{}"
# create an instance of EditNode from a JSON string
edit_node_instance = EditNode.from_json(json)
# print the JSON string representation of the object
print(EditNode.to_json())

# convert the object into a dict
edit_node_dict = edit_node_instance.to_dict()
# create an instance of EditNode from a dict
edit_node_from_dict = EditNode.from_dict(edit_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


