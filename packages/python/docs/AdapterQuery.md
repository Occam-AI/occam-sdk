# AdapterQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.adapter_query import AdapterQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AdapterQuery from a JSON string
adapter_query_instance = AdapterQuery.from_json(json)
# print the JSON string representation of the object
print(AdapterQuery.to_json())

# convert the object into a dict
adapter_query_dict = adapter_query_instance.to_dict()
# create an instance of AdapterQuery from a dict
adapter_query_from_dict = AdapterQuery.from_dict(adapter_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


