# UserUpdatePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from occam_sdk.models.user_update_password_request import UserUpdatePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdatePasswordRequest from a JSON string
user_update_password_request_instance = UserUpdatePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(UserUpdatePasswordRequest.to_json())

# convert the object into a dict
user_update_password_request_dict = user_update_password_request_instance.to_dict()
# create an instance of UserUpdatePasswordRequest from a dict
user_update_password_request_from_dict = UserUpdatePasswordRequest.from_dict(user_update_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


