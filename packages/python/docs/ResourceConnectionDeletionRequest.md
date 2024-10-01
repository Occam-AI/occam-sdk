# ResourceConnectionDeletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uuid** | **str** |  | [optional] 
**user_to_resource_uuid** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.resource_connection_deletion_request import ResourceConnectionDeletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConnectionDeletionRequest from a JSON string
resource_connection_deletion_request_instance = ResourceConnectionDeletionRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceConnectionDeletionRequest.to_json())

# convert the object into a dict
resource_connection_deletion_request_dict = resource_connection_deletion_request_instance.to_dict()
# create an instance of ResourceConnectionDeletionRequest from a dict
resource_connection_deletion_request_from_dict = ResourceConnectionDeletionRequest.from_dict(resource_connection_deletion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


