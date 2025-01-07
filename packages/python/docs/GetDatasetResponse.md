# GetDatasetResponse


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
from occam_sdk.models.get_dataset_response import GetDatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetResponse from a JSON string
get_dataset_response_instance = GetDatasetResponse.from_json(json)
# print the JSON string representation of the object
print(GetDatasetResponse.to_json())

# convert the object into a dict
get_dataset_response_dict = get_dataset_response_instance.to_dict()
# create an instance of GetDatasetResponse from a dict
get_dataset_response_from_dict = GetDatasetResponse.from_dict(get_dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


