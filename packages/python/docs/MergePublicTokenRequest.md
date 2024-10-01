# MergePublicTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_token** | **str** |  | 
**resource_name** | **str** |  | 

## Example

```python
from occam_sdk.models.merge_public_token_request import MergePublicTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergePublicTokenRequest from a JSON string
merge_public_token_request_instance = MergePublicTokenRequest.from_json(json)
# print the JSON string representation of the object
print(MergePublicTokenRequest.to_json())

# convert the object into a dict
merge_public_token_request_dict = merge_public_token_request_instance.to_dict()
# create an instance of MergePublicTokenRequest from a dict
merge_public_token_request_from_dict = MergePublicTokenRequest.from_dict(merge_public_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


