# GetUserPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**var_date** | **datetime** |  | 
**category** | **str** |  | 
**run_metrics** | [**RunMetrics**](RunMetrics.md) |  | 
**status** | **str** |  | 
**run_status** | **str** |  | 
**organization** | [**GetOrganizationResponse**](GetOrganizationResponse.md) |  | 

## Example

```python
from occam_sdk.models.get_user_plan_response import GetUserPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPlanResponse from a JSON string
get_user_plan_response_instance = GetUserPlanResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserPlanResponse.to_json())

# convert the object into a dict
get_user_plan_response_dict = get_user_plan_response_instance.to_dict()
# create an instance of GetUserPlanResponse from a dict
get_user_plan_response_from_dict = GetUserPlanResponse.from_dict(get_user_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


