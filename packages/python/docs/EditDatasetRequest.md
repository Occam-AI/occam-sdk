# EditDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.edit_dataset_request import EditDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditDatasetRequest from a JSON string
edit_dataset_request_instance = EditDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(EditDatasetRequest.to_json())

# convert the object into a dict
edit_dataset_request_dict = edit_dataset_request_instance.to_dict()
# create an instance of EditDatasetRequest from a dict
edit_dataset_request_from_dict = EditDatasetRequest.from_dict(edit_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


