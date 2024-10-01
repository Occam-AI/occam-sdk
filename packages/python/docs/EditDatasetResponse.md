# EditDatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.edit_dataset_response import EditDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditDatasetResponse from a JSON string
edit_dataset_response_instance = EditDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(EditDatasetResponse.to_json())

# convert the object into a dict
edit_dataset_response_dict = edit_dataset_response_instance.to_dict()
# create an instance of EditDatasetResponse from a dict
edit_dataset_response_from_dict = EditDatasetResponse.from_dict(edit_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


