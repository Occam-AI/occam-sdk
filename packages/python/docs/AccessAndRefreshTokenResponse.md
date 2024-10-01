# AccessAndRefreshTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | [optional] [default to 'Bearer']
**access_token** | **str** |  | 
**expires_at** | **int** |  | 
**refresh_token** | **str** |  | 
**refresh_token_expires_at** | **int** |  | 

## Example

```python
from occam_sdk.models.access_and_refresh_token_response import AccessAndRefreshTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessAndRefreshTokenResponse from a JSON string
access_and_refresh_token_response_instance = AccessAndRefreshTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AccessAndRefreshTokenResponse.to_json())

# convert the object into a dict
access_and_refresh_token_response_dict = access_and_refresh_token_response_instance.to_dict()
# create an instance of AccessAndRefreshTokenResponse from a dict
access_and_refresh_token_response_from_dict = AccessAndRefreshTokenResponse.from_dict(access_and_refresh_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


