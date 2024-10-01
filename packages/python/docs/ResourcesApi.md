# occam_sdk.ResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credential_credentials_post**](ResourcesApi.md#add_credential_credentials_post) | **POST** /credentials/ | Add Credential
[**delete_credential_credentials_uuid_delete**](ResourcesApi.md#delete_credential_credentials_uuid_delete) | **DELETE** /credentials/{uuid} | Delete Credential
[**resource_add_datasource**](ResourcesApi.md#resource_add_datasource) | **POST** /resources/ | Add Resource
[**resource_connect**](ResourcesApi.md#resource_connect) | **POST** /resources/{resource_uuid}/connection | Update User Resource Connection
[**resource_datasource_schemas**](ResourcesApi.md#resource_datasource_schemas) | **GET** /resources/datasource/schema | Get Datasource Schemas
[**resource_delete_connection**](ResourcesApi.md#resource_delete_connection) | **DELETE** /resources/connection | Delete Connection
[**resource_get**](ResourcesApi.md#resource_get) | **GET** /resources/{resource_uuid} | Get Resource
[**resource_list**](ResourcesApi.md#resource_list) | **GET** /resources/ | Get Resources
[**resource_list_files**](ResourcesApi.md#resource_list_files) | **GET** /resources/{resource_uuid}/files | Get Resource Files
[**resource_refresh**](ResourcesApi.md#resource_refresh) | **POST** /resources/refresh | Refresh Resources
[**resource_schema**](ResourcesApi.md#resource_schema) | **GET** /resources/schema | Get Resource Schema
[**resource_schemas**](ResourcesApi.md#resource_schemas) | **GET** /resources/schemas | Get Datasources Schemas
[**resource_tool_schemas**](ResourcesApi.md#resource_tool_schemas) | **GET** /resources/tool/schema | Get Tools Schemas
[**resource_update**](ResourcesApi.md#resource_update) | **POST** /resources/{resource_uuid}/update | Update User Resource
[**upload_file_credentials_fileupload_post**](ResourcesApi.md#upload_file_credentials_fileupload_post) | **POST** /credentials/fileupload | Upload File


# **add_credential_credentials_post**
> UUIDResponse add_credential_credentials_post(credentials_data_partial_request)

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
    api_instance = occam_sdk.ResourcesApi(api_client)
    credentials_data_partial_request = occam_sdk.CredentialsDataPartialRequest() # CredentialsDataPartialRequest | 

    try:
        # Add Credential
        api_response = api_instance.add_credential_credentials_post(credentials_data_partial_request)
        print("The response of ResourcesApi->add_credential_credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->add_credential_credentials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_data_partial_request** | [**CredentialsDataPartialRequest**](CredentialsDataPartialRequest.md)|  | 

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
> object delete_credential_credentials_uuid_delete(uuid)

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
    api_instance = occam_sdk.ResourcesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete Credential
        api_response = api_instance.delete_credential_credentials_uuid_delete(uuid)
        print("The response of ResourcesApi->delete_credential_credentials_uuid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->delete_credential_credentials_uuid_delete: %s\n" % e)
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

# **resource_add_datasource**
> AddDataSourceResponse resource_add_datasource(add_data_source_request, include_datasets=include_datasets)

Add Resource

Add a data source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.add_data_source_request import AddDataSourceRequest
from occam_sdk.models.add_data_source_response import AddDataSourceResponse
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    add_data_source_request = occam_sdk.AddDataSourceRequest() # AddDataSourceRequest | 
    include_datasets = False # bool |  (optional) (default to False)

    try:
        # Add Resource
        api_response = api_instance.resource_add_datasource(add_data_source_request, include_datasets=include_datasets)
        print("The response of ResourcesApi->resource_add_datasource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_add_datasource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_data_source_request** | [**AddDataSourceRequest**](AddDataSourceRequest.md)|  | 
 **include_datasets** | **bool**|  | [optional] [default to False]

### Return type

[**AddDataSourceResponse**](AddDataSourceResponse.md)

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

# **resource_connect**
> GetResourceResponse resource_connect(resource_uuid, add_user_to_resource_request, include_datasets=include_datasets)

Update User Resource Connection

Connect a user to resource connection

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.add_user_to_resource_request import AddUserToResourceRequest
from occam_sdk.models.get_resource_response import GetResourceResponse
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    add_user_to_resource_request = occam_sdk.AddUserToResourceRequest() # AddUserToResourceRequest | 
    include_datasets = False # bool |  (optional) (default to False)

    try:
        # Update User Resource Connection
        api_response = api_instance.resource_connect(resource_uuid, add_user_to_resource_request, include_datasets=include_datasets)
        print("The response of ResourcesApi->resource_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **add_user_to_resource_request** | [**AddUserToResourceRequest**](AddUserToResourceRequest.md)|  | 
 **include_datasets** | **bool**|  | [optional] [default to False]

### Return type

[**GetResourceResponse**](GetResourceResponse.md)

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

# **resource_datasource_schemas**
> List[ResponseResourceInfo] resource_datasource_schemas()

Get Datasource Schemas

Returns JSON schema of all sources

### Example


```python
import occam_sdk
from occam_sdk.models.response_resource_info import ResponseResourceInfo
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
    api_instance = occam_sdk.ResourcesApi(api_client)

    try:
        # Get Datasource Schemas
        api_response = api_instance.resource_datasource_schemas()
        print("The response of ResourcesApi->resource_datasource_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_datasource_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ResponseResourceInfo]**](ResponseResourceInfo.md)

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

# **resource_delete_connection**
> object resource_delete_connection(resource_connection_deletion_request)

Delete Connection

Delete connection based on the connection's uuid

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.resource_connection_deletion_request import ResourceConnectionDeletionRequest
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    resource_connection_deletion_request = occam_sdk.ResourceConnectionDeletionRequest() # ResourceConnectionDeletionRequest | 

    try:
        # Delete Connection
        api_response = api_instance.resource_delete_connection(resource_connection_deletion_request)
        print("The response of ResourcesApi->resource_delete_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_delete_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_connection_deletion_request** | [**ResourceConnectionDeletionRequest**](ResourceConnectionDeletionRequest.md)|  | 

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

# **resource_get**
> GetResourceResponse resource_get(resource_uuid, include_datasets=include_datasets)

Get Resource

Get information about the data source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_resource_response import GetResourceResponse
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    include_datasets = False # bool |  (optional) (default to False)

    try:
        # Get Resource
        api_response = api_instance.resource_get(resource_uuid, include_datasets=include_datasets)
        print("The response of ResourcesApi->resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **include_datasets** | **bool**|  | [optional] [default to False]

### Return type

[**GetResourceResponse**](GetResourceResponse.md)

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

# **resource_list**
> GetResourcesResponse resource_list(include_datasets=include_datasets)

Get Resources

Get all resources with their connection status

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_resources_response import GetResourcesResponse
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    include_datasets = False # bool |  (optional) (default to False)

    try:
        # Get Resources
        api_response = api_instance.resource_list(include_datasets=include_datasets)
        print("The response of ResourcesApi->resource_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_datasets** | **bool**|  | [optional] [default to False]

### Return type

[**GetResourcesResponse**](GetResourcesResponse.md)

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

# **resource_list_files**
> Dict[str, ListedKey] resource_list_files(resource_uuid, key=key)

Get Resource Files

List files in directory. Only valid for FileSystem resources

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.listed_key import ListedKey
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    key = 'key_example' # str |  (optional)

    try:
        # Get Resource Files
        api_response = api_instance.resource_list_files(resource_uuid, key=key)
        print("The response of ResourcesApi->resource_list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **key** | **str**|  | [optional] 

### Return type

[**Dict[str, ListedKey]**](ListedKey.md)

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

# **resource_refresh**
> object resource_refresh(refresh_resources_request)

Refresh Resources

Refresh resources based on a refresh entry point

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.refresh_resources_request import RefreshResourcesRequest
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    refresh_resources_request = occam_sdk.RefreshResourcesRequest() # RefreshResourcesRequest | 

    try:
        # Refresh Resources
        api_response = api_instance.resource_refresh(refresh_resources_request)
        print("The response of ResourcesApi->resource_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_resources_request** | [**RefreshResourcesRequest**](RefreshResourcesRequest.md)|  | 

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

# **resource_schema**
> GetResourceSchemaResponse resource_schema(resource_kind)

Get Resource Schema

Returns the JSON schema of the connector for the asked resource type

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_resource_schema_response import GetResourceSchemaResponse
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    resource_kind = 'resource_kind_example' # str | 

    try:
        # Get Resource Schema
        api_response = api_instance.resource_schema(resource_kind)
        print("The response of ResourcesApi->resource_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | **str**|  | 

### Return type

[**GetResourceSchemaResponse**](GetResourceSchemaResponse.md)

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

# **resource_schemas**
> List[ResponseResourceInfo] resource_schemas()

Get Datasources Schemas

Returns JSON schema of all resources

### Example


```python
import occam_sdk
from occam_sdk.models.response_resource_info import ResponseResourceInfo
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
    api_instance = occam_sdk.ResourcesApi(api_client)

    try:
        # Get Datasources Schemas
        api_response = api_instance.resource_schemas()
        print("The response of ResourcesApi->resource_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ResponseResourceInfo]**](ResponseResourceInfo.md)

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

# **resource_tool_schemas**
> List[ResponseResourceInfo] resource_tool_schemas()

Get Tools Schemas

Returns JSON schema of all tools

### Example


```python
import occam_sdk
from occam_sdk.models.response_resource_info import ResponseResourceInfo
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
    api_instance = occam_sdk.ResourcesApi(api_client)

    try:
        # Get Tools Schemas
        api_response = api_instance.resource_tool_schemas()
        print("The response of ResourcesApi->resource_tool_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_tool_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ResponseResourceInfo]**](ResponseResourceInfo.md)

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

# **resource_update**
> object resource_update(resource_uuid, update_user_resource_request)

Update User Resource

Update a user resource

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.update_user_resource_request import UpdateUserResourceRequest
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    update_user_resource_request = occam_sdk.UpdateUserResourceRequest() # UpdateUserResourceRequest | 

    try:
        # Update User Resource
        api_response = api_instance.resource_update(resource_uuid, update_user_resource_request)
        print("The response of ResourcesApi->resource_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **update_user_resource_request** | [**UpdateUserResourceRequest**](UpdateUserResourceRequest.md)|  | 

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

# **upload_file_credentials_fileupload_post**
> FileUploadResponse upload_file_credentials_fileupload_post(file)

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
    api_instance = occam_sdk.ResourcesApi(api_client)
    file = None # bytearray | 

    try:
        # Upload File
        api_response = api_instance.upload_file_credentials_fileupload_post(file)
        print("The response of ResourcesApi->upload_file_credentials_fileupload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->upload_file_credentials_fileupload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

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

