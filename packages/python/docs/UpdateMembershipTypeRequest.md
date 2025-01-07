# UpdateMembershipTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** |  | 
**membership_type** | [**MembershipType**](MembershipType.md) |  | 

## Example

```python
from occam_sdk.models.update_membership_type_request import UpdateMembershipTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembershipTypeRequest from a JSON string
update_membership_type_request_instance = UpdateMembershipTypeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMembershipTypeRequest.to_json())

# convert the object into a dict
update_membership_type_request_dict = update_membership_type_request_instance.to_dict()
# create an instance of UpdateMembershipTypeRequest from a dict
update_membership_type_request_from_dict = UpdateMembershipTypeRequest.from_dict(update_membership_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


