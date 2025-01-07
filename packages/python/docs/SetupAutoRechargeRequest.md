# SetupAutoRechargeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_amount_dollars** | **int** |  | 
**bring_balance_up_to_dollars** | **int** |  | 

## Example

```python
from occam_sdk.models.setup_auto_recharge_request import SetupAutoRechargeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupAutoRechargeRequest from a JSON string
setup_auto_recharge_request_instance = SetupAutoRechargeRequest.from_json(json)
# print the JSON string representation of the object
print(SetupAutoRechargeRequest.to_json())

# convert the object into a dict
setup_auto_recharge_request_dict = setup_auto_recharge_request_instance.to_dict()
# create an instance of SetupAutoRechargeRequest from a dict
setup_auto_recharge_request_from_dict = SetupAutoRechargeRequest.from_dict(setup_auto_recharge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


