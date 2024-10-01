# AddDataSourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**kind** | **str** |  | 
**kind_display_name** | **str** |  | 
**instance_display_name** | **str** |  | [optional] 
**short_description** | **str** |  | 
**long_description** | **str** |  | 
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
**is_template** | **bool** |  | [optional] [default to False]
**is_scannable** | **bool** |  | [optional] [default to False]
**is_template_instance** | **bool** |  | [optional] [default to False]
**credential_uuid** | **str** |  | [optional] 
**datasets** | [**List[GetDatasetResponse]**](GetDatasetResponse.md) |  | [optional] 
**input_fields** | [**List[BasicFieldInfo]**](BasicFieldInfo.md) |  | [optional] 
**params_model** | **object** |  | [optional] 
**output_fields** | [**List[BasicFieldInfo]**](BasicFieldInfo.md) |  | [optional] 

## Example

```python
from occam_sdk.models.add_data_source_response import AddDataSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDataSourceResponse from a JSON string
add_data_source_response_instance = AddDataSourceResponse.from_json(json)
# print the JSON string representation of the object
print(AddDataSourceResponse.to_json())

# convert the object into a dict
add_data_source_response_dict = add_data_source_response_instance.to_dict()
# create an instance of AddDataSourceResponse from a dict
add_data_source_response_from_dict = AddDataSourceResponse.from_dict(add_data_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


