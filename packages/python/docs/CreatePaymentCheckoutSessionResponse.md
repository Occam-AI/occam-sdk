# CreatePaymentCheckoutSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stripe_checkout_session_id** | **str** |  | 
**stripe_checkout_url** | **str** |  | 
**customer_id** | **str** |  | 

## Example

```python
from occam_sdk.models.create_payment_checkout_session_response import CreatePaymentCheckoutSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentCheckoutSessionResponse from a JSON string
create_payment_checkout_session_response_instance = CreatePaymentCheckoutSessionResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentCheckoutSessionResponse.to_json())

# convert the object into a dict
create_payment_checkout_session_response_dict = create_payment_checkout_session_response_instance.to_dict()
# create an instance of CreatePaymentCheckoutSessionResponse from a dict
create_payment_checkout_session_response_from_dict = CreatePaymentCheckoutSessionResponse.from_dict(create_payment_checkout_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


