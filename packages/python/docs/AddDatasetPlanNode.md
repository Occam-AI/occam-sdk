# AddDatasetPlanNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role_description** | **str** |  | 
**node_id** | **int** |  | [optional] 
**data_source_access_name** | **str** |  | [optional] 
**is_proposed** | **bool** |  | [optional] [default to False]
**plan_id** | **str** |  | 
**type** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.add_dataset_plan_node import AddDatasetPlanNode

# TODO update the JSON string below
json = "{}"
# create an instance of AddDatasetPlanNode from a JSON string
add_dataset_plan_node_instance = AddDatasetPlanNode.from_json(json)
# print the JSON string representation of the object
print(AddDatasetPlanNode.to_json())

# convert the object into a dict
add_dataset_plan_node_dict = add_dataset_plan_node_instance.to_dict()
# create an instance of AddDatasetPlanNode from a dict
add_dataset_plan_node_from_dict = AddDatasetPlanNode.from_dict(add_dataset_plan_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


