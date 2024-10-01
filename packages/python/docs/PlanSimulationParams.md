# PlanSimulationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**mode** | **str** |  | [optional] 
**max_duration_seconds** | **int** |  | [optional] 

## Example

```python
from occam_sdk.models.plan_simulation_params import PlanSimulationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSimulationParams from a JSON string
plan_simulation_params_instance = PlanSimulationParams.from_json(json)
# print the JSON string representation of the object
print(PlanSimulationParams.to_json())

# convert the object into a dict
plan_simulation_params_dict = plan_simulation_params_instance.to_dict()
# create an instance of PlanSimulationParams from a dict
plan_simulation_params_from_dict = PlanSimulationParams.from_dict(plan_simulation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


