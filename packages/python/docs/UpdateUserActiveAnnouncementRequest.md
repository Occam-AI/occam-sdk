# UpdateUserActiveAnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_credits_announcement_active** | **bool** |  | [optional] 
**auto_recharge_failed_announcement_active** | **bool** |  | [optional] 

## Example

```python
from occam_sdk.models.update_user_active_announcement_request import UpdateUserActiveAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserActiveAnnouncementRequest from a JSON string
update_user_active_announcement_request_instance = UpdateUserActiveAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserActiveAnnouncementRequest.to_json())

# convert the object into a dict
update_user_active_announcement_request_dict = update_user_active_announcement_request_instance.to_dict()
# create an instance of UpdateUserActiveAnnouncementRequest from a dict
update_user_active_announcement_request_from_dict = UpdateUserActiveAnnouncementRequest.from_dict(update_user_active_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


