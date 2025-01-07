# occam_sdk.PaymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout_session_payment_create_checkout_session_post**](PaymentApi.md#create_checkout_session_payment_create_checkout_session_post) | **POST** /payment/create-checkout-session | Create Checkout Session
[**disable_auto_recharge_payment_disable_auto_recharge_post**](PaymentApi.md#disable_auto_recharge_payment_disable_auto_recharge_post) | **POST** /payment/disable-auto-recharge | Disable Auto Recharge
[**get_user_details_payment_user_details_get**](PaymentApi.md#get_user_details_payment_user_details_get) | **GET** /payment/user-details | Get User Details
[**get_user_payment_methods_payment_user_payment_methods_get**](PaymentApi.md#get_user_payment_methods_payment_user_payment_methods_get) | **GET** /payment/user-payment-methods | Get User Payment Methods
[**manage_payment_method_payment_manage_payment_method_post**](PaymentApi.md#manage_payment_method_payment_manage_payment_method_post) | **POST** /payment/manage-payment-method | Manage Payment Method
[**setup_auto_recharge_payment_setup_auto_recharge_post**](PaymentApi.md#setup_auto_recharge_payment_setup_auto_recharge_post) | **POST** /payment/setup-auto-recharge | Setup Auto Recharge
[**test_cancel_payment_cancel_post**](PaymentApi.md#test_cancel_payment_cancel_post) | **POST** /payment/cancel | Test Cancel
[**test_success_payment_success_post**](PaymentApi.md#test_success_payment_success_post) | **POST** /payment/success | Test Success
[**webhook_payment_webhook_post**](PaymentApi.md#webhook_payment_webhook_post) | **POST** /payment/webhook | Webhook


# **create_checkout_session_payment_create_checkout_session_post**
> CreatePaymentCheckoutSessionResponse create_checkout_session_payment_create_checkout_session_post(create_payment_checkout_session_request, settings=settings)

Create Checkout Session

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.create_payment_checkout_session_request import CreatePaymentCheckoutSessionRequest
from occam_sdk.models.create_payment_checkout_session_response import CreatePaymentCheckoutSessionResponse
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)
    create_payment_checkout_session_request = occam_sdk.CreatePaymentCheckoutSessionRequest() # CreatePaymentCheckoutSessionRequest | 
    settings = None # object |  (optional)

    try:
        # Create Checkout Session
        api_response = api_instance.create_checkout_session_payment_create_checkout_session_post(create_payment_checkout_session_request, settings=settings)
        print("The response of PaymentApi->create_checkout_session_payment_create_checkout_session_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_checkout_session_payment_create_checkout_session_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_checkout_session_request** | [**CreatePaymentCheckoutSessionRequest**](CreatePaymentCheckoutSessionRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**CreatePaymentCheckoutSessionResponse**](CreatePaymentCheckoutSessionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_auto_recharge_payment_disable_auto_recharge_post**
> object disable_auto_recharge_payment_disable_auto_recharge_post(settings=settings)

Disable Auto Recharge

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)
    settings = None # object |  (optional)

    try:
        # Disable Auto Recharge
        api_response = api_instance.disable_auto_recharge_payment_disable_auto_recharge_post(settings=settings)
        print("The response of PaymentApi->disable_auto_recharge_payment_disable_auto_recharge_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->disable_auto_recharge_payment_disable_auto_recharge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_details_payment_user_details_get**
> GetUserPaymentDetailsResponse get_user_details_payment_user_details_get(settings=settings)

Get User Details

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_user_payment_details_response import GetUserPaymentDetailsResponse
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)
    settings = None # object |  (optional)

    try:
        # Get User Details
        api_response = api_instance.get_user_details_payment_user_details_get(settings=settings)
        print("The response of PaymentApi->get_user_details_payment_user_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_user_details_payment_user_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**GetUserPaymentDetailsResponse**](GetUserPaymentDetailsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_payment_methods_payment_user_payment_methods_get**
> UserStripePaymentMethodsResponse get_user_payment_methods_payment_user_payment_methods_get(settings=settings)

Get User Payment Methods

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.user_stripe_payment_methods_response import UserStripePaymentMethodsResponse
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)
    settings = None # object |  (optional)

    try:
        # Get User Payment Methods
        api_response = api_instance.get_user_payment_methods_payment_user_payment_methods_get(settings=settings)
        print("The response of PaymentApi->get_user_payment_methods_payment_user_payment_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_user_payment_methods_payment_user_payment_methods_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**UserStripePaymentMethodsResponse**](UserStripePaymentMethodsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_payment_method_payment_manage_payment_method_post**
> ManagePaymentMethodResponse manage_payment_method_payment_manage_payment_method_post(settings=settings)

Manage Payment Method

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.manage_payment_method_response import ManagePaymentMethodResponse
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)
    settings = None # object |  (optional)

    try:
        # Manage Payment Method
        api_response = api_instance.manage_payment_method_payment_manage_payment_method_post(settings=settings)
        print("The response of PaymentApi->manage_payment_method_payment_manage_payment_method_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->manage_payment_method_payment_manage_payment_method_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**ManagePaymentMethodResponse**](ManagePaymentMethodResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_auto_recharge_payment_setup_auto_recharge_post**
> object setup_auto_recharge_payment_setup_auto_recharge_post(setup_auto_recharge_request, settings=settings)

Setup Auto Recharge

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.setup_auto_recharge_request import SetupAutoRechargeRequest
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)
    setup_auto_recharge_request = occam_sdk.SetupAutoRechargeRequest() # SetupAutoRechargeRequest | 
    settings = None # object |  (optional)

    try:
        # Setup Auto Recharge
        api_response = api_instance.setup_auto_recharge_payment_setup_auto_recharge_post(setup_auto_recharge_request, settings=settings)
        print("The response of PaymentApi->setup_auto_recharge_payment_setup_auto_recharge_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->setup_auto_recharge_payment_setup_auto_recharge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_auto_recharge_request** | [**SetupAutoRechargeRequest**](SetupAutoRechargeRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_cancel_payment_cancel_post**
> object test_cancel_payment_cancel_post()

Test Cancel

### Example


```python
import occam_sdk
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)

    try:
        # Test Cancel
        api_response = api_instance.test_cancel_payment_cancel_post()
        print("The response of PaymentApi->test_cancel_payment_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->test_cancel_payment_cancel_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_success_payment_success_post**
> object test_success_payment_success_post()

Test Success

### Example


```python
import occam_sdk
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)

    try:
        # Test Success
        api_response = api_instance.test_success_payment_success_post()
        print("The response of PaymentApi->test_success_payment_success_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->test_success_payment_success_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_payment_webhook_post**
> object webhook_payment_webhook_post()

Webhook

Stripe webhook endpoint. This endpoint is called by Stripe after a transaction is completed. That is when we updated user's payment record with the payment details for this transaction.

### Example


```python
import occam_sdk
from occam_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = occam_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with occam_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = occam_sdk.PaymentApi(api_client)

    try:
        # Webhook
        api_response = api_instance.webhook_payment_webhook_post()
        print("The response of PaymentApi->webhook_payment_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->webhook_payment_webhook_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

