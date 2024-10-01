# occam_sdk.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_current_user_users_me_delete**](UserApi.md#delete_current_user_users_me_delete) | **DELETE** /users/me | Delete Current User
[**get_connector_schemas_connectors_schemas_get**](UserApi.md#get_connector_schemas_connectors_schemas_get) | **GET** /connectors/schemas | Get Connector Schemas
[**google_oauth_end_integrations_oauth_google_end_get**](UserApi.md#google_oauth_end_integrations_oauth_google_end_get) | **GET** /integrations/oauth/google/end | Google Oauth End
[**isolated_oauth_end_integrations_oauth_isolated_end_get**](UserApi.md#isolated_oauth_end_integrations_oauth_isolated_end_get) | **GET** /integrations/oauth/isolated/end | Isolated Oauth End
[**merge_confirm_integrations_merge_confirm_post**](UserApi.md#merge_confirm_integrations_merge_confirm_post) | **POST** /integrations/merge/confirm | Merge Confirm
[**merge_link_token_integrations_merge_link_token_get**](UserApi.md#merge_link_token_integrations_merge_link_token_get) | **GET** /integrations/merge/link_token | Merge Link Token
[**oauth_end_integrations_oauth_end_get**](UserApi.md#oauth_end_integrations_oauth_end_get) | **GET** /integrations/oauth/end | Oauth End
[**oauth_start_integrations_oauth_start_get**](UserApi.md#oauth_start_integrations_oauth_start_get) | **GET** /integrations/oauth/start | Oauth Start
[**read_current_user_users_me_get**](UserApi.md#read_current_user_users_me_get) | **GET** /users/me | Read Current User
[**register_new_user_users_register_post**](UserApi.md#register_new_user_users_register_post) | **POST** /users/register | Register New User
[**reset_current_user_password_users_reset_password_post**](UserApi.md#reset_current_user_password_users_reset_password_post) | **POST** /users/reset-password | Reset Current User Password


# **delete_current_user_users_me_delete**
> delete_current_user_users_me_delete()

Delete Current User

Delete current user

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
    api_instance = occam_sdk.UserApi(api_client)

    try:
        # Delete Current User
        api_instance.delete_current_user_users_me_delete()
    except Exception as e:
        print("Exception when calling UserApi->delete_current_user_users_me_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_schemas_connectors_schemas_get**
> List[ConnectorSchema] get_connector_schemas_connectors_schemas_get()

Get Connector Schemas

Get the JSON schema for all available connectors

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.connector_schema import ConnectorSchema
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
    api_instance = occam_sdk.UserApi(api_client)

    try:
        # Get Connector Schemas
        api_response = api_instance.get_connector_schemas_connectors_schemas_get()
        print("The response of UserApi->get_connector_schemas_connectors_schemas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_connector_schemas_connectors_schemas_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConnectorSchema]**](ConnectorSchema.md)

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

# **google_oauth_end_integrations_oauth_google_end_get**
> object google_oauth_end_integrations_oauth_google_end_get(state, code)

Google Oauth End

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
    api_instance = occam_sdk.UserApi(api_client)
    state = None # object | 
    code = None # object | 

    try:
        # Google Oauth End
        api_response = api_instance.google_oauth_end_integrations_oauth_google_end_get(state, code)
        print("The response of UserApi->google_oauth_end_integrations_oauth_google_end_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->google_oauth_end_integrations_oauth_google_end_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**object**](.md)|  | 
 **code** | [**object**](.md)|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isolated_oauth_end_integrations_oauth_isolated_end_get**
> UUIDResponse isolated_oauth_end_integrations_oauth_isolated_end_get(state)

Isolated Oauth End

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.uuid_response import UUIDResponse
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
    api_instance = occam_sdk.UserApi(api_client)
    state = 'state_example' # str | 

    try:
        # Isolated Oauth End
        api_response = api_instance.isolated_oauth_end_integrations_oauth_isolated_end_get(state)
        print("The response of UserApi->isolated_oauth_end_integrations_oauth_isolated_end_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->isolated_oauth_end_integrations_oauth_isolated_end_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**UUIDResponse**](UUIDResponse.md)

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

# **merge_confirm_integrations_merge_confirm_post**
> UUIDResponse merge_confirm_integrations_merge_confirm_post(merge_public_token_request)

Merge Confirm

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.merge_public_token_request import MergePublicTokenRequest
from occam_sdk.models.uuid_response import UUIDResponse
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
    api_instance = occam_sdk.UserApi(api_client)
    merge_public_token_request = occam_sdk.MergePublicTokenRequest() # MergePublicTokenRequest | 

    try:
        # Merge Confirm
        api_response = api_instance.merge_confirm_integrations_merge_confirm_post(merge_public_token_request)
        print("The response of UserApi->merge_confirm_integrations_merge_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->merge_confirm_integrations_merge_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_public_token_request** | [**MergePublicTokenRequest**](MergePublicTokenRequest.md)|  | 

### Return type

[**UUIDResponse**](UUIDResponse.md)

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

# **merge_link_token_integrations_merge_link_token_get**
> MergeLinkTokenResponse merge_link_token_integrations_merge_link_token_get(resource_kind)

Merge Link Token

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.merge_link_token_response import MergeLinkTokenResponse
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
    api_instance = occam_sdk.UserApi(api_client)
    resource_kind = 'resource_kind_example' # str | 

    try:
        # Merge Link Token
        api_response = api_instance.merge_link_token_integrations_merge_link_token_get(resource_kind)
        print("The response of UserApi->merge_link_token_integrations_merge_link_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->merge_link_token_integrations_merge_link_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | **str**|  | 

### Return type

[**MergeLinkTokenResponse**](MergeLinkTokenResponse.md)

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

# **oauth_end_integrations_oauth_end_get**
> object oauth_end_integrations_oauth_end_get(state, code)

Oauth End

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
    api_instance = occam_sdk.UserApi(api_client)
    state = None # object | 
    code = None # object | 

    try:
        # Oauth End
        api_response = api_instance.oauth_end_integrations_oauth_end_get(state, code)
        print("The response of UserApi->oauth_end_integrations_oauth_end_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->oauth_end_integrations_oauth_end_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**object**](.md)|  | 
 **code** | [**object**](.md)|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_start_integrations_oauth_start_get**
> RedirectToResponse oauth_start_integrations_oauth_start_get(resource_kind, redirect_url)

Oauth Start

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.redirect_to_response import RedirectToResponse
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
    api_instance = occam_sdk.UserApi(api_client)
    resource_kind = 'resource_kind_example' # str | 
    redirect_url = 'redirect_url_example' # str | 

    try:
        # Oauth Start
        api_response = api_instance.oauth_start_integrations_oauth_start_get(resource_kind, redirect_url)
        print("The response of UserApi->oauth_start_integrations_oauth_start_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->oauth_start_integrations_oauth_start_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | **str**|  | 
 **redirect_url** | **str**|  | 

### Return type

[**RedirectToResponse**](RedirectToResponse.md)

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

# **read_current_user_users_me_get**
> UserResponse read_current_user_users_me_get()

Read Current User

Get current user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.user_response import UserResponse
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
    api_instance = occam_sdk.UserApi(api_client)

    try:
        # Read Current User
        api_response = api_instance.read_current_user_users_me_get()
        print("The response of UserApi->read_current_user_users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->read_current_user_users_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

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

# **register_new_user_users_register_post**
> UserResponse register_new_user_users_register_post(user_create_request)

Register New User

Create new user

### Example


```python
import occam_sdk
from occam_sdk.models.user_create_request import UserCreateRequest
from occam_sdk.models.user_response import UserResponse
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
    api_instance = occam_sdk.UserApi(api_client)
    user_create_request = occam_sdk.UserCreateRequest() # UserCreateRequest | 

    try:
        # Register New User
        api_response = api_instance.register_new_user_users_register_post(user_create_request)
        print("The response of UserApi->register_new_user_users_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->register_new_user_users_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_request** | [**UserCreateRequest**](UserCreateRequest.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_current_user_password_users_reset_password_post**
> reset_current_user_password_users_reset_password_post(user_update_password_request)

Reset Current User Password

Update current user password

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.user_update_password_request import UserUpdatePasswordRequest
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
    api_instance = occam_sdk.UserApi(api_client)
    user_update_password_request = occam_sdk.UserUpdatePasswordRequest() # UserUpdatePasswordRequest | 

    try:
        # Reset Current User Password
        api_instance.reset_current_user_password_users_reset_password_post(user_update_password_request)
    except Exception as e:
        print("Exception when calling UserApi->reset_current_user_password_users_reset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update_password_request** | [**UserUpdatePasswordRequest**](UserUpdatePasswordRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

