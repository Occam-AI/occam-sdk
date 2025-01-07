# ManagePaymentMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_session_url** | **str** |  | 
**portal_session_id** | **str** |  | 

## Example

```python
from occam_sdk.models.manage_payment_method_response import ManagePaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManagePaymentMethodResponse from a JSON string
manage_payment_method_response_instance = ManagePaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print(ManagePaymentMethodResponse.to_json())

# convert the object into a dict
manage_payment_method_response_dict = manage_payment_method_response_instance.to_dict()
# create an instance of ManagePaymentMethodResponse from a dict
manage_payment_method_response_from_dict = ManagePaymentMethodResponse.from_dict(manage_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


