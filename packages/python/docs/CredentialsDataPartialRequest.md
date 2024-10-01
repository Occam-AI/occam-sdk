# CredentialsDataPartialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_type** | **str** |  | 
**credential_data** | **object** |  | 

## Example

```python
from occam_sdk.models.credentials_data_partial_request import CredentialsDataPartialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsDataPartialRequest from a JSON string
credentials_data_partial_request_instance = CredentialsDataPartialRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialsDataPartialRequest.to_json())

# convert the object into a dict
credentials_data_partial_request_dict = credentials_data_partial_request_instance.to_dict()
# create an instance of CredentialsDataPartialRequest from a dict
credentials_data_partial_request_from_dict = CredentialsDataPartialRequest.from_dict(credentials_data_partial_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


