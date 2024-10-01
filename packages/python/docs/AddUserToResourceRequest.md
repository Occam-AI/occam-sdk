# AddUserToResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** |  | [optional] 
**credential_uuid** | **str** |  | [optional] 
**instance_display_name** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.add_user_to_resource_request import AddUserToResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserToResourceRequest from a JSON string
add_user_to_resource_request_instance = AddUserToResourceRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserToResourceRequest.to_json())

# convert the object into a dict
add_user_to_resource_request_dict = add_user_to_resource_request_instance.to_dict()
# create an instance of AddUserToResourceRequest from a dict
add_user_to_resource_request_from_dict = AddUserToResourceRequest.from_dict(add_user_to_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


