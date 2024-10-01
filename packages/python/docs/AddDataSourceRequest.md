# AddDataSourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_display_name** | **str** |  | 
**needs_credentials** | **bool** |  | 
**use_credential_as_default** | **bool** |  | 
**credential_uuid** | **str** |  | [optional] 
**resource_type** | **str** |  | 
**address** | **object** |  | 
**strictness** | [**ResourceStrictness**](ResourceStrictness.md) |  | 
**description** | **str** |  | [optional] 
**allowed_user_uuids** | **List[str]** |  | [optional] 

## Example

```python
from occam_sdk.models.add_data_source_request import AddDataSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDataSourceRequest from a JSON string
add_data_source_request_instance = AddDataSourceRequest.from_json(json)
# print the JSON string representation of the object
print(AddDataSourceRequest.to_json())

# convert the object into a dict
add_data_source_request_dict = add_data_source_request_instance.to_dict()
# create an instance of AddDataSourceRequest from a dict
add_data_source_request_from_dict = AddDataSourceRequest.from_dict(add_data_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


