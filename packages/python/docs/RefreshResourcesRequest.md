# RefreshResourcesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_entry_point** | [**RefreshEntryPoint**](RefreshEntryPoint.md) |  | 

## Example

```python
from occam_sdk.models.refresh_resources_request import RefreshResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshResourcesRequest from a JSON string
refresh_resources_request_instance = RefreshResourcesRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshResourcesRequest.to_json())

# convert the object into a dict
refresh_resources_request_dict = refresh_resources_request_instance.to_dict()
# create an instance of RefreshResourcesRequest from a dict
refresh_resources_request_from_dict = RefreshResourcesRequest.from_dict(refresh_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


