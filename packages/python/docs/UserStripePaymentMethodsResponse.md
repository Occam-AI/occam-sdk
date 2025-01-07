# UserStripePaymentMethodsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_stripe_customer** | **bool** |  | 
**customer_id** | **str** |  | [optional] 
**payment_methods** | **List[str]** |  | [optional] 

## Example

```python
from occam_sdk.models.user_stripe_payment_methods_response import UserStripePaymentMethodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserStripePaymentMethodsResponse from a JSON string
user_stripe_payment_methods_response_instance = UserStripePaymentMethodsResponse.from_json(json)
# print the JSON string representation of the object
print(UserStripePaymentMethodsResponse.to_json())

# convert the object into a dict
user_stripe_payment_methods_response_dict = user_stripe_payment_methods_response_instance.to_dict()
# create an instance of UserStripePaymentMethodsResponse from a dict
user_stripe_payment_methods_response_from_dict = UserStripePaymentMethodsResponse.from_dict(user_stripe_payment_methods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


