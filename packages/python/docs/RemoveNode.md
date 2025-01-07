# RemoveNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**node_id** | **int** |  | 
**type** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.remove_node import RemoveNode

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveNode from a JSON string
remove_node_instance = RemoveNode.from_json(json)
# print the JSON string representation of the object
print(RemoveNode.to_json())

# convert the object into a dict
remove_node_dict = remove_node_instance.to_dict()
# create an instance of RemoveNode from a dict
remove_node_from_dict = RemoveNode.from_dict(remove_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


