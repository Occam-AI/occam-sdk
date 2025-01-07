# occam_sdk.IntegrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credential_credentials_post**](IntegrationApi.md#add_credential_credentials_post) | **POST** /credentials/ | Add Credential
[**delete_credential_credentials_uuid_delete**](IntegrationApi.md#delete_credential_credentials_uuid_delete) | **DELETE** /credentials/{uuid} | Delete Credential
[**get_connector_schemas_connectors_schemas_get**](IntegrationApi.md#get_connector_schemas_connectors_schemas_get) | **GET** /connectors/schemas | Get Connector Schemas
[**google_oauth_end_integrations_oauth_google_end_get**](IntegrationApi.md#google_oauth_end_integrations_oauth_google_end_get) | **GET** /integrations/oauth/google/end | Google Oauth End
[**isolated_oauth_end_integrations_oauth_isolated_end_get**](IntegrationApi.md#isolated_oauth_end_integrations_oauth_isolated_end_get) | **GET** /integrations/oauth/isolated/end | Isolated Oauth End
[**merge_confirm_integrations_merge_confirm_post**](IntegrationApi.md#merge_confirm_integrations_merge_confirm_post) | **POST** /integrations/merge/confirm | Merge Confirm
[**merge_link_token_integrations_merge_link_token_get**](IntegrationApi.md#merge_link_token_integrations_merge_link_token_get) | **GET** /integrations/merge/link_token | Merge Link Token
[**oauth_end_integrations_oauth_end_get**](IntegrationApi.md#oauth_end_integrations_oauth_end_get) | **GET** /integrations/oauth/end | Oauth End
[**oauth_start_integrations_oauth_start_get**](IntegrationApi.md#oauth_start_integrations_oauth_start_get) | **GET** /integrations/oauth/start | Oauth Start
[**upload_file_credentials_fileupload_post**](IntegrationApi.md#upload_file_credentials_fileupload_post) | **POST** /credentials/fileupload | Upload File


# **add_credential_credentials_post**
> UUIDResponse add_credential_credentials_post(credentials_data_partial_request, settings=settings)

Add Credential

Add a crededential

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.credentials_data_partial_request import CredentialsDataPartialRequest
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
    api_instance = occam_sdk.IntegrationApi(api_client)
    credentials_data_partial_request = occam_sdk.CredentialsDataPartialRequest() # CredentialsDataPartialRequest | 
    settings = None # object |  (optional)

    try:
        # Add Credential
        api_response = api_instance.add_credential_credentials_post(credentials_data_partial_request, settings=settings)
        print("The response of IntegrationApi->add_credential_credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->add_credential_credentials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_data_partial_request** | [**CredentialsDataPartialRequest**](CredentialsDataPartialRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

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

# **delete_credential_credentials_uuid_delete**
> object delete_credential_credentials_uuid_delete(uuid, settings=settings)

Delete Credential

delete a crededential

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    uuid = 'uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Delete Credential
        api_response = api_instance.delete_credential_credentials_uuid_delete(uuid, settings=settings)
        print("The response of IntegrationApi->delete_credential_credentials_uuid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->delete_credential_credentials_uuid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
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

# **get_connector_schemas_connectors_schemas_get**
> List[ConnectorSchema] get_connector_schemas_connectors_schemas_get(settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    settings = None # object |  (optional)

    try:
        # Get Connector Schemas
        api_response = api_instance.get_connector_schemas_connectors_schemas_get(settings=settings)
        print("The response of IntegrationApi->get_connector_schemas_connectors_schemas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->get_connector_schemas_connectors_schemas_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**object**](.md)|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_oauth_end_integrations_oauth_google_end_get**
> object google_oauth_end_integrations_oauth_google_end_get(state, code, settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    state = None # object | 
    code = None # object | 
    settings = None # object |  (optional)

    try:
        # Google Oauth End
        api_response = api_instance.google_oauth_end_integrations_oauth_google_end_get(state, code, settings=settings)
        print("The response of IntegrationApi->google_oauth_end_integrations_oauth_google_end_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->google_oauth_end_integrations_oauth_google_end_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**object**](.md)|  | 
 **code** | [**object**](.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

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
> UUIDResponse isolated_oauth_end_integrations_oauth_isolated_end_get(state, settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    state = 'state_example' # str | 
    settings = None # object |  (optional)

    try:
        # Isolated Oauth End
        api_response = api_instance.isolated_oauth_end_integrations_oauth_isolated_end_get(state, settings=settings)
        print("The response of IntegrationApi->isolated_oauth_end_integrations_oauth_isolated_end_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->isolated_oauth_end_integrations_oauth_isolated_end_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

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
> UUIDResponse merge_confirm_integrations_merge_confirm_post(merge_public_token_request, settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    merge_public_token_request = occam_sdk.MergePublicTokenRequest() # MergePublicTokenRequest | 
    settings = None # object |  (optional)

    try:
        # Merge Confirm
        api_response = api_instance.merge_confirm_integrations_merge_confirm_post(merge_public_token_request, settings=settings)
        print("The response of IntegrationApi->merge_confirm_integrations_merge_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->merge_confirm_integrations_merge_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_public_token_request** | [**MergePublicTokenRequest**](MergePublicTokenRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

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
> MergeLinkTokenResponse merge_link_token_integrations_merge_link_token_get(resource_kind, settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    resource_kind = 'resource_kind_example' # str | 
    settings = None # object |  (optional)

    try:
        # Merge Link Token
        api_response = api_instance.merge_link_token_integrations_merge_link_token_get(resource_kind, settings=settings)
        print("The response of IntegrationApi->merge_link_token_integrations_merge_link_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->merge_link_token_integrations_merge_link_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

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
> object oauth_end_integrations_oauth_end_get(state, code, settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    state = None # object | 
    code = None # object | 
    settings = None # object |  (optional)

    try:
        # Oauth End
        api_response = api_instance.oauth_end_integrations_oauth_end_get(state, code, settings=settings)
        print("The response of IntegrationApi->oauth_end_integrations_oauth_end_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->oauth_end_integrations_oauth_end_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**object**](.md)|  | 
 **code** | [**object**](.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

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
> RedirectToResponse oauth_start_integrations_oauth_start_get(resource_kind, redirect_url, settings=settings)

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
    api_instance = occam_sdk.IntegrationApi(api_client)
    resource_kind = 'resource_kind_example' # str | 
    redirect_url = 'redirect_url_example' # str | 
    settings = None # object |  (optional)

    try:
        # Oauth Start
        api_response = api_instance.oauth_start_integrations_oauth_start_get(resource_kind, redirect_url, settings=settings)
        print("The response of IntegrationApi->oauth_start_integrations_oauth_start_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->oauth_start_integrations_oauth_start_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | **str**|  | 
 **redirect_url** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

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

# **upload_file_credentials_fileupload_post**
> FileUploadResponse upload_file_credentials_fileupload_post(file, settings=settings)

Upload File

Endpoint used to upload files related to credentials

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.file_upload_response import FileUploadResponse
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
    api_instance = occam_sdk.IntegrationApi(api_client)
    file = None # bytearray | 
    settings = None # object |  (optional)

    try:
        # Upload File
        api_response = api_instance.upload_file_credentials_fileupload_post(file, settings=settings)
        print("The response of IntegrationApi->upload_file_credentials_fileupload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->upload_file_credentials_fileupload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | No &#x60;Authorization&#x60; access token header, token is invalid or user removed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

