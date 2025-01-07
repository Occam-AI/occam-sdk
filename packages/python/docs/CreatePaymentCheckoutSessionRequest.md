# CreatePaymentCheckoutSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** |  | [optional] 
**purchase_amount** | **int** |  | [optional] 
**product_type** | **str** |  | 

## Example

```python
from occam_sdk.models.create_payment_checkout_session_request import CreatePaymentCheckoutSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentCheckoutSessionRequest from a JSON string
create_payment_checkout_session_request_instance = CreatePaymentCheckoutSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentCheckoutSessionRequest.to_json())

# convert the object into a dict
create_payment_checkout_session_request_dict = create_payment_checkout_session_request_instance.to_dict()
# create an instance of CreatePaymentCheckoutSessionRequest from a dict
create_payment_checkout_session_request_from_dict = CreatePaymentCheckoutSessionRequest.from_dict(create_payment_checkout_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


