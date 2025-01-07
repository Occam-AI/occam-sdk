# AddToolPlanNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role_description** | **str** |  | 
**node_id** | **int** |  | [optional] 
**plan_id** | **str** |  | 
**params** | **Dict[str, object]** |  | [optional] 
**adapter_query** | [**AdapterQuery**](AdapterQuery.md) |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.add_tool_plan_node import AddToolPlanNode

# TODO update the JSON string below
json = "{}"
# create an instance of AddToolPlanNode from a JSON string
add_tool_plan_node_instance = AddToolPlanNode.from_json(json)
# print the JSON string representation of the object
print(AddToolPlanNode.to_json())

# convert the object into a dict
add_tool_plan_node_dict = add_tool_plan_node_instance.to_dict()
# create an instance of AddToolPlanNode from a dict
add_tool_plan_node_from_dict = AddToolPlanNode.from_dict(add_tool_plan_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


