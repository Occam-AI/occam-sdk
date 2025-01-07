# GetResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**kind** | **str** |  | 
**kind_display_name** | **str** |  | 
**instance_display_name** | **str** |  | [optional] 
**kind_short_description** | **str** |  | 
**kind_long_description** | **str** |  | 
**description** | **str** |  | [optional] 
**icon** | **str** |  | 
**category** | **str** |  | 
**category_rank** | **int** |  | 
**address** | **object** |  | 
**needs_credentials** | **bool** |  | 
**is_datasource** | **bool** |  | 
**strictness** | [**ResourceStrictness**](ResourceStrictness.md) |  | 
**is_connected** | **bool** |  | 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | 
**subtool_kinds** | **List[str]** |  | [optional] 
**connection_uuid** | **str** |  | [optional] 
**from_code** | **bool** |  | [optional] [default to False]
**is_template** | **bool** |  | [optional] [default to False]
**is_scannable** | **bool** |  | [optional] [default to False]
**is_template_instance** | **bool** |  | [optional] [default to False]
**credential_uuid** | **str** |  | [optional] 
**credential_metadata** | **object** |  | [optional] 
**datasets** | [**List[GetDatasetResponse]**](GetDatasetResponse.md) |  | [optional] 
**input_fields** | [**List[BasicFieldInfo]**](BasicFieldInfo.md) |  | [optional] 
**params_model** | **object** |  | [optional] 
**output_fields** | [**List[BasicFieldInfo]**](BasicFieldInfo.md) |  | [optional] 
**access_name** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.get_resource_response import GetResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceResponse from a JSON string
get_resource_response_instance = GetResourceResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourceResponse.to_json())

# convert the object into a dict
get_resource_response_dict = get_resource_response_instance.to_dict()
# create an instance of GetResourceResponse from a dict
get_resource_response_from_dict = GetResourceResponse.from_dict(get_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


