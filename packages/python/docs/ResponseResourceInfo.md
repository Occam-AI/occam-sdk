# ResponseResourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**kind_display_name** | **str** |  | 
**category** | **str** |  | 
**icon** | **str** |  | 
**kind_short_description** | **str** |  | 
**kind_long_description** | **str** |  | 

## Example

```python
from occam_sdk.models.response_resource_info import ResponseResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseResourceInfo from a JSON string
response_resource_info_instance = ResponseResourceInfo.from_json(json)
# print the JSON string representation of the object
print(ResponseResourceInfo.to_json())

# convert the object into a dict
response_resource_info_dict = response_resource_info_instance.to_dict()
# create an instance of ResponseResourceInfo from a dict
response_resource_info_from_dict = ResponseResourceInfo.from_dict(response_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


