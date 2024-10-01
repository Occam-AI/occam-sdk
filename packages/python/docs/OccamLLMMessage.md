# OccamLLMMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**Content**](Content.md) |  | 
**role** | [**LLMRole**](LLMRole.md) |  | 
**name** | **str** |  | [optional] 
**parsed** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.occam_llm_message import OccamLLMMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OccamLLMMessage from a JSON string
occam_llm_message_instance = OccamLLMMessage.from_json(json)
# print the JSON string representation of the object
print(OccamLLMMessage.to_json())

# convert the object into a dict
occam_llm_message_dict = occam_llm_message_instance.to_dict()
# create an instance of OccamLLMMessage from a dict
occam_llm_message_from_dict = OccamLLMMessage.from_dict(occam_llm_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


