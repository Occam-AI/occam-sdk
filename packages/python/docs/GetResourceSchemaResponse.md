# GetResourceSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **object** |  | [optional] 
**oauth** | [**OAuthConfig**](OAuthConfig.md) |  | [optional] 

## Example

```python
from occam_sdk.models.get_resource_schema_response import GetResourceSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceSchemaResponse from a JSON string
get_resource_schema_response_instance = GetResourceSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourceSchemaResponse.to_json())

# convert the object into a dict
get_resource_schema_response_dict = get_resource_schema_response_instance.to_dict()
# create an instance of GetResourceSchemaResponse from a dict
get_resource_schema_response_from_dict = GetResourceSchemaResponse.from_dict(get_resource_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


