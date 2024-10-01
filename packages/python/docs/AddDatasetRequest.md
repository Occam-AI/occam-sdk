# AddDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**name** | **str** |  | 
**content** | **object** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.add_dataset_request import AddDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDatasetRequest from a JSON string
add_dataset_request_instance = AddDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(AddDatasetRequest.to_json())

# convert the object into a dict
add_dataset_request_dict = add_dataset_request_instance.to_dict()
# create an instance of AddDatasetRequest from a dict
add_dataset_request_from_dict = AddDatasetRequest.from_dict(add_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


