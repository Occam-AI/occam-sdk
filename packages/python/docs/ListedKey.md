# ListedKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**is_dir** | **bool** |  | 
**depth** | **int** |  | 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 

## Example

```python
from occam_sdk.models.listed_key import ListedKey

# TODO update the JSON string below
json = "{}"
# create an instance of ListedKey from a JSON string
listed_key_instance = ListedKey.from_json(json)
# print the JSON string representation of the object
print(ListedKey.to_json())

# convert the object into a dict
listed_key_dict = listed_key_instance.to_dict()
# create an instance of ListedKey from a dict
listed_key_from_dict = ListedKey.from_dict(listed_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


