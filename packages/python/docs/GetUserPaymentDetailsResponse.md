# GetUserPaymentDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_transactions** | **int** |  | 
**successful_transactions** | **int** |  | 
**failed_transactions** | **int** |  | 
**last_transaction_date** | **datetime** |  | [optional] 
**last_transaction_was_successful** | **bool** |  | [optional] 
**topup_suggested_amount** | **int** |  | [optional] 
**default_payment_method_configured** | **bool** |  | 
**auto_recharge_active** | **bool** |  | 
**auto_recharge_threshold_amount** | **int** |  | [optional] 
**auto_recharge_bring_balance_up_to_amount** | **int** |  | [optional] 
**available_balance** | **int** |  | [optional] 
**used_balance** | **int** |  | [optional] 
**available_credits** | **int** |  | [optional] 
**used_credits** | **int** |  | [optional] 
**free_credits_announcement_active** | **bool** |  | [optional] 
**auto_recharge_failed_announcement_active** | **bool** |  | [optional] 

## Example

```python
from occam_sdk.models.get_user_payment_details_response import GetUserPaymentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPaymentDetailsResponse from a JSON string
get_user_payment_details_response_instance = GetUserPaymentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserPaymentDetailsResponse.to_json())

# convert the object into a dict
get_user_payment_details_response_dict = get_user_payment_details_response_instance.to_dict()
# create an instance of GetUserPaymentDetailsResponse from a dict
get_user_payment_details_response_from_dict = GetUserPaymentDetailsResponse.from_dict(get_user_payment_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


