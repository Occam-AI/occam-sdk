# UpdateUserResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_display_name** | **str** |  | 

## Example

```python
from occam_sdk.models.update_user_resource_request import UpdateUserResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserResourceRequest from a JSON string
update_user_resource_request_instance = UpdateUserResourceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserResourceRequest.to_json())

# convert the object into a dict
update_user_resource_request_dict = update_user_resource_request_instance.to_dict()
# create an instance of UpdateUserResourceRequest from a dict
update_user_resource_request_from_dict = UpdateUserResourceRequest.from_dict(update_user_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


