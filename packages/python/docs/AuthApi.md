# occam_sdk.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login**](AuthApi.md#auth_login) | **POST** /auth/access-token | Login Access Token
[**auth_refresh**](AuthApi.md#auth_refresh) | **POST** /auth/refresh-token | Refresh Token
[**auth_token_from_key**](AuthApi.md#auth_token_from_key) | **GET** /auth/access-token | Login Access Token Via Key


# **auth_login**
> AccessAndRefreshTokenResponse auth_login(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login Access Token

OAuth2 compatible token, get an access token for future requests using username and password

### Example


```python
import occam_sdk
from occam_sdk.models.access_and_refresh_token_response import AccessAndRefreshTokenResponse
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
    api_instance = occam_sdk.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login Access Token
        api_response = api_instance.auth_login(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->auth_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**AccessAndRefreshTokenResponse**](AccessAndRefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid email or password |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh**
> AccessAndRefreshTokenResponse auth_refresh(refresh_token_request)

Refresh Token

OAuth2 compatible token, get an access token for future requests using refresh token

### Example


```python
import occam_sdk
from occam_sdk.models.access_and_refresh_token_response import AccessAndRefreshTokenResponse
from occam_sdk.models.refresh_token_request import RefreshTokenRequest
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
    api_instance = occam_sdk.AuthApi(api_client)
    refresh_token_request = occam_sdk.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh Token
        api_response = api_instance.auth_refresh(refresh_token_request)
        print("The response of AuthApi->auth_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**AccessAndRefreshTokenResponse**](AccessAndRefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Refresh token expired or is already used |  -  |
**404** | Refresh token does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_token_from_key**
> AccessTokenResponse auth_token_from_key(key)

Login Access Token Via Key

OAuth2 compatible token, get an access token for future requests using username and password

### Example


```python
import occam_sdk
from occam_sdk.models.access_token_response import AccessTokenResponse
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
    api_instance = occam_sdk.AuthApi(api_client)
    key = 'key_example' # str | 

    try:
        # Login Access Token Via Key
        api_response = api_instance.auth_token_from_key(key)
        print("The response of AuthApi->auth_token_from_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_token_from_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid email or password |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

