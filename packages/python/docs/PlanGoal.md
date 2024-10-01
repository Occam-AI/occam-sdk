# PlanGoal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_name_user_generated** | **bool** |  | [optional] [default to True]
**chat_messages** | [**List[OccamLLMMessage]**](OccamLLMMessage.md) |  | [optional] 
**user_id** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**params** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.plan_goal import PlanGoal

# TODO update the JSON string below
json = "{}"
# create an instance of PlanGoal from a JSON string
plan_goal_instance = PlanGoal.from_json(json)
# print the JSON string representation of the object
print(PlanGoal.to_json())

# convert the object into a dict
plan_goal_dict = plan_goal_instance.to_dict()
# create an instance of PlanGoal from a dict
plan_goal_from_dict = PlanGoal.from_dict(plan_goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


