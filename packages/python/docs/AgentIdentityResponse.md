# AgentIdentityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**base_agent** | **object** |  | 
**type** | [**AgentType**](AgentType.md) |  | 
**role** | [**AgentRole**](AgentRole.md) |  | 
**role_embedding_vector** | **List[float]** |  | [optional] 
**short_role_description** | **str** |  | [optional] 
**long_role_description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**slack_handle** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**prompt** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**dynamic_spec** | [**AnyOf**](AnyOf.md) |  | [optional] 
**is_base_agent** | **bool** |  | [optional] [default to False]
**params_model_schema** | **object** |  | 
**inputs_model_schema** | **object** |  | 
**outputs_model_schema** | **object** |  | 

## Example

```python
from occam_sdk.models.agent_identity_response import AgentIdentityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentIdentityResponse from a JSON string
agent_identity_response_instance = AgentIdentityResponse.from_json(json)
# print the JSON string representation of the object
print(AgentIdentityResponse.to_json())

# convert the object into a dict
agent_identity_response_dict = agent_identity_response_instance.to_dict()
# create an instance of AgentIdentityResponse from a dict
agent_identity_response_from_dict = AgentIdentityResponse.from_dict(agent_identity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


