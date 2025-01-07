# AddDatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**name** | **str** |  | 
**content** | **object** |  | 
**address_summary** | **str** |  | [optional] [default to '/temporary/placeholder']
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | 
**description** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.add_dataset_response import AddDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDatasetResponse from a JSON string
add_dataset_response_instance = AddDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(AddDatasetResponse.to_json())

# convert the object into a dict
add_dataset_response_dict = add_dataset_response_instance.to_dict()
# create an instance of AddDatasetResponse from a dict
add_dataset_response_from_dict = AddDatasetResponse.from_dict(add_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


