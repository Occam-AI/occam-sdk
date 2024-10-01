# GetResourcesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | [**List[GetResourceResponse]**](GetResourceResponse.md) |  | 
**unconnected** | [**List[GetResourceResponse]**](GetResourceResponse.md) |  | 

## Example

```python
from occam_sdk.models.get_resources_response import GetResourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourcesResponse from a JSON string
get_resources_response_instance = GetResourcesResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourcesResponse.to_json())

# convert the object into a dict
get_resources_response_dict = get_resources_response_instance.to_dict()
# create an instance of GetResourcesResponse from a dict
get_resources_response_from_dict = GetResourcesResponse.from_dict(get_resources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


