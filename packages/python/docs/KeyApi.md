# occam_sdk.KeyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_keys_put**](KeyApi.md#create_key_keys_put) | **PUT** /keys/ | Create Key
[**delete_key_keys_uuid_delete**](KeyApi.md#delete_key_keys_uuid_delete) | **DELETE** /keys/{uuid} | Delete Key
[**get_key_usage_keys_uuid_usage_get**](KeyApi.md#get_key_usage_keys_uuid_usage_get) | **GET** /keys/{uuid}/usage | Get Key Usage
[**list_keys_keys_get**](KeyApi.md#list_keys_keys_get) | **GET** /keys/ | List Keys


# **create_key_keys_put**
> VisibleAPIKeyResponse create_key_keys_put(put_api_key_request)

Create Key

Create an API key for the calling user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.put_api_key_request import PutAPIKeyRequest
from occam_sdk.models.visible_api_key_response import VisibleAPIKeyResponse
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
    api_instance = occam_sdk.KeyApi(api_client)
    put_api_key_request = occam_sdk.PutAPIKeyRequest() # PutAPIKeyRequest | 

    try:
        # Create Key
        api_response = api_instance.create_key_keys_put(put_api_key_request)
        print("The response of KeyApi->create_key_keys_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->create_key_keys_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_api_key_request** | [**PutAPIKeyRequest**](PutAPIKeyRequest.md)|  | 

### Return type

[**VisibleAPIKeyResponse**](VisibleAPIKeyResponse.md)

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

# **delete_key_keys_uuid_delete**
> object delete_key_keys_uuid_delete(uuid)

Delete Key

Delete an API key

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
    api_instance = occam_sdk.KeyApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete Key
        api_response = api_instance.delete_key_keys_uuid_delete(uuid)
        print("The response of KeyApi->delete_key_keys_uuid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->delete_key_keys_uuid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

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

# **get_key_usage_keys_uuid_usage_get**
> APIKeyUsageResponse get_key_usage_keys_uuid_usage_get(uuid)

Get Key Usage

Get usage of a given API key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.api_key_usage_response import APIKeyUsageResponse
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
    api_instance = occam_sdk.KeyApi(api_client)
    uuid = None # object | 

    try:
        # Get Key Usage
        api_response = api_instance.get_key_usage_keys_uuid_usage_get(uuid)
        print("The response of KeyApi->get_key_usage_keys_uuid_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->get_key_usage_keys_uuid_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**object**](.md)|  | 

### Return type

[**APIKeyUsageResponse**](APIKeyUsageResponse.md)

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

# **list_keys_keys_get**
> List[HiddenAPIKeyResponse] list_keys_keys_get()

List Keys

List API keys of the calling user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.hidden_api_key_response import HiddenAPIKeyResponse
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
    api_instance = occam_sdk.KeyApi(api_client)

    try:
        # List Keys
        api_response = api_instance.list_keys_keys_get()
        print("The response of KeyApi->list_keys_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->list_keys_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[HiddenAPIKeyResponse]**](HiddenAPIKeyResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

