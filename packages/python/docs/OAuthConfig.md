# OAuthConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **str** |  | 
**flow_type** | **str** |  | 
**provider** | **str** |  | 

## Example

```python
from occam_sdk.models.o_auth_config import OAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthConfig from a JSON string
o_auth_config_instance = OAuthConfig.from_json(json)
# print the JSON string representation of the object
print(OAuthConfig.to_json())

# convert the object into a dict
o_auth_config_dict = o_auth_config_instance.to_dict()
# create an instance of OAuthConfig from a dict
o_auth_config_from_dict = OAuthConfig.from_dict(o_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


