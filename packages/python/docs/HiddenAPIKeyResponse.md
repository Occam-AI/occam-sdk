# HiddenAPIKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**name** | **str** |  | 
**api_key** | **str** |  | 
**created** | **datetime** |  | 
**last_used** | **datetime** |  | 

## Example

```python
from occam_sdk.models.hidden_api_key_response import HiddenAPIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HiddenAPIKeyResponse from a JSON string
hidden_api_key_response_instance = HiddenAPIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(HiddenAPIKeyResponse.to_json())

# convert the object into a dict
hidden_api_key_response_dict = hidden_api_key_response_instance.to_dict()
# create an instance of HiddenAPIKeyResponse from a dict
hidden_api_key_response_from_dict = HiddenAPIKeyResponse.from_dict(hidden_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


