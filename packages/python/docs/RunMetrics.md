# RunMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_minutes** | **float** |  | 
**cost_dollars** | **float** |  | 
**success_rate** | **float** |  | 
**metrics_are_estimates** | **bool** |  | [optional] 

## Example

```python
from occam_sdk.models.run_metrics import RunMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of RunMetrics from a JSON string
run_metrics_instance = RunMetrics.from_json(json)
# print the JSON string representation of the object
print(RunMetrics.to_json())

# convert the object into a dict
run_metrics_dict = run_metrics_instance.to_dict()
# create an instance of RunMetrics from a dict
run_metrics_from_dict = RunMetrics.from_dict(run_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


