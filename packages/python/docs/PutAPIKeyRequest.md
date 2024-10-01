# PutAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from occam_sdk.models.put_api_key_request import PutAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutAPIKeyRequest from a JSON string
put_api_key_request_instance = PutAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PutAPIKeyRequest.to_json())

# convert the object into a dict
put_api_key_request_dict = put_api_key_request_instance.to_dict()
# create an instance of PutAPIKeyRequest from a dict
put_api_key_request_from_dict = PutAPIKeyRequest.from_dict(put_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


