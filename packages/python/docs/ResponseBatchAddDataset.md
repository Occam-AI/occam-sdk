# ResponseBatchAddDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_name** | **str** |  | 
**content** | **object** |  | [optional] 
**address_summary** | **str** |  | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**error** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.response_batch_add_dataset import ResponseBatchAddDataset

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBatchAddDataset from a JSON string
response_batch_add_dataset_instance = ResponseBatchAddDataset.from_json(json)
# print the JSON string representation of the object
print(ResponseBatchAddDataset.to_json())

# convert the object into a dict
response_batch_add_dataset_dict = response_batch_add_dataset_instance.to_dict()
# create an instance of ResponseBatchAddDataset from a dict
response_batch_add_dataset_from_dict = ResponseBatchAddDataset.from_dict(response_batch_add_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


