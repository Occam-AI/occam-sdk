# VisibleAPIKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**api_key** | **str** |  | 

## Example

```python
from occam_sdk.models.visible_api_key_response import VisibleAPIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VisibleAPIKeyResponse from a JSON string
visible_api_key_response_instance = VisibleAPIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(VisibleAPIKeyResponse.to_json())

# convert the object into a dict
visible_api_key_response_dict = visible_api_key_response_instance.to_dict()
# create an instance of VisibleAPIKeyResponse from a dict
visible_api_key_response_from_dict = VisibleAPIKeyResponse.from_dict(visible_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


