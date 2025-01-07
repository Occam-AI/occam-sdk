# occam_sdk.ResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credential_credentials_post**](ResourcesApi.md#add_credential_credentials_post) | **POST** /credentials/ | Add Credential
[**add_dataset_resources_source_uuid_dataset_post**](ResourcesApi.md#add_dataset_resources_source_uuid_dataset_post) | **POST** /resources/{source_uuid}/dataset | Add Dataset
[**dataset_allowed_schemas**](ResourcesApi.md#dataset_allowed_schemas) | **GET** /resources/{uuid}/dataset/schema | Get Datasource Dataset Schemas
[**dataset_batch_add**](ResourcesApi.md#dataset_batch_add) | **POST** /resources/{source_uuid}/datasets | Batch Add Dataset
[**dataset_delete**](ResourcesApi.md#dataset_delete) | **DELETE** /resources/{uuid}/dataset/{dataset_uuid} | Delete Dataset
[**dataset_edit**](ResourcesApi.md#dataset_edit) | **POST** /resources/{uuid}/dataset/{dataset_uuid} | Edit Dataset
[**dataset_get**](ResourcesApi.md#dataset_get) | **GET** /resources/{uuid}/dataset/{dataset_uuid} | Get Dataset
[**dataset_list**](ResourcesApi.md#dataset_list) | **GET** /resources/{uuid}/dataset | Get Datasets
[**delete_credential_credentials_uuid_delete**](ResourcesApi.md#delete_credential_credentials_uuid_delete) | **DELETE** /credentials/{uuid} | Delete Credential
[**resource_add_datasource**](ResourcesApi.md#resource_add_datasource) | **POST** /resources/ | Add Resource
[**resource_connect**](ResourcesApi.md#resource_connect) | **POST** /resources/{uuid}/connection | Update User Resource Connection
[**resource_datasource_schemas**](ResourcesApi.md#resource_datasource_schemas) | **GET** /resources/datasource/schema | Get Datasources Schemas
[**resource_delete_connection**](ResourcesApi.md#resource_delete_connection) | **DELETE** /resources/connection | Delete Connection
[**resource_get**](ResourcesApi.md#resource_get) | **GET** /resources/{uuid} | Get Resource
[**resource_get_files**](ResourcesApi.md#resource_get_files) | **GET** /resources/{uuid}/files | Get Resource Files
[**resource_list**](ResourcesApi.md#resource_list) | **GET** /resources/ | Get Resources
[**resource_refresh**](ResourcesApi.md#resource_refresh) | **POST** /resources/refresh | Refresh Resources
[**resource_schema**](ResourcesApi.md#resource_schema) | **GET** /resources/schema | Get Resource Schema
[**resource_schemas**](ResourcesApi.md#resource_schemas) | **GET** /resources/schemas | Get Datasources Schemas
[**resource_tools_schemas**](ResourcesApi.md#resource_tools_schemas) | **GET** /resources/tool/schema | Get Tools Schemas
[**resource_update**](ResourcesApi.md#resource_update) | **POST** /resources/{uuid}/update | Update User Resource
[**upload_file_credentials_fileupload_post**](ResourcesApi.md#upload_file_credentials_fileupload_post) | **POST** /credentials/fileupload | Upload File


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
    api_instance = occam_sdk.ResourcesApi(api_client)
    credentials_data_partial_request = occam_sdk.CredentialsDataPartialRequest() # CredentialsDataPartialRequest | 
    settings = None # object |  (optional)

    try:
        # Add Credential
        api_response = api_instance.add_credential_credentials_post(credentials_data_partial_request, settings=settings)
        print("The response of ResourcesApi->add_credential_credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->add_credential_credentials_post: %s\n" % e)
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

# **add_dataset_resources_source_uuid_dataset_post**
> AddDatasetResponse add_dataset_resources_source_uuid_dataset_post(source_uuid, add_dataset_request, settings=settings)

Add Dataset

Add a data dataset to an existing source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.add_dataset_request import AddDatasetRequest
from occam_sdk.models.add_dataset_response import AddDatasetResponse
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
    source_uuid = 'source_uuid_example' # str | 
    add_dataset_request = occam_sdk.AddDatasetRequest() # AddDatasetRequest | 
    settings = None # object |  (optional)

    try:
        # Add Dataset
        api_response = api_instance.add_dataset_resources_source_uuid_dataset_post(source_uuid, add_dataset_request, settings=settings)
        print("The response of ResourcesApi->add_dataset_resources_source_uuid_dataset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->add_dataset_resources_source_uuid_dataset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uuid** | **str**|  | 
 **add_dataset_request** | [**AddDatasetRequest**](AddDatasetRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**AddDatasetResponse**](AddDatasetResponse.md)

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

# **dataset_allowed_schemas**
> ResponseDatasourceDatasetSchemas dataset_allowed_schemas(uuid, settings=settings)

Get Datasource Dataset Schemas

Returns the JSON schemas for datasets allowed by a datasource

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.response_datasource_dataset_schemas import ResponseDatasourceDatasetSchemas
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
    settings = None # object |  (optional)

    try:
        # Get Datasource Dataset Schemas
        api_response = api_instance.dataset_allowed_schemas(uuid, settings=settings)
        print("The response of ResourcesApi->dataset_allowed_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->dataset_allowed_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**ResponseDatasourceDatasetSchemas**](ResponseDatasourceDatasetSchemas.md)

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

# **dataset_batch_add**
> List[ResponseBatchAddDataset] dataset_batch_add(source_uuid, add_dataset_request, settings=settings)

Batch Add Dataset

Add multiple datasets to an existing source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.add_dataset_request import AddDatasetRequest
from occam_sdk.models.response_batch_add_dataset import ResponseBatchAddDataset
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
    source_uuid = 'source_uuid_example' # str | 
    add_dataset_request = [occam_sdk.AddDatasetRequest()] # List[AddDatasetRequest] | 
    settings = None # object |  (optional)

    try:
        # Batch Add Dataset
        api_response = api_instance.dataset_batch_add(source_uuid, add_dataset_request, settings=settings)
        print("The response of ResourcesApi->dataset_batch_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->dataset_batch_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uuid** | **str**|  | 
 **add_dataset_request** | [**List[AddDatasetRequest]**](AddDatasetRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**List[ResponseBatchAddDataset]**](ResponseBatchAddDataset.md)

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

# **dataset_delete**
> UUIDResponse dataset_delete(uuid, dataset_uuid, settings=settings)

Delete Dataset

Delete a dataset for the data source

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
    api_instance = occam_sdk.ResourcesApi(api_client)
    uuid = 'uuid_example' # str | 
    dataset_uuid = 'dataset_uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Delete Dataset
        api_response = api_instance.dataset_delete(uuid, dataset_uuid, settings=settings)
        print("The response of ResourcesApi->dataset_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->dataset_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **dataset_uuid** | **str**|  | 
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

# **dataset_edit**
> EditDatasetResponse dataset_edit(uuid, dataset_uuid, edit_dataset_request, settings=settings)

Edit Dataset

Edit a dataset for the data source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.edit_dataset_request import EditDatasetRequest
from occam_sdk.models.edit_dataset_response import EditDatasetResponse
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
    dataset_uuid = 'dataset_uuid_example' # str | 
    edit_dataset_request = occam_sdk.EditDatasetRequest() # EditDatasetRequest | 
    settings = None # object |  (optional)

    try:
        # Edit Dataset
        api_response = api_instance.dataset_edit(uuid, dataset_uuid, edit_dataset_request, settings=settings)
        print("The response of ResourcesApi->dataset_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->dataset_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **dataset_uuid** | **str**|  | 
 **edit_dataset_request** | [**EditDatasetRequest**](EditDatasetRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**EditDatasetResponse**](EditDatasetResponse.md)

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

# **dataset_get**
> GetDatasetResponse dataset_get(uuid, dataset_uuid, settings=settings)

Get Dataset

Get a dataset for the data source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_dataset_response import GetDatasetResponse
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
    dataset_uuid = 'dataset_uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Get Dataset
        api_response = api_instance.dataset_get(uuid, dataset_uuid, settings=settings)
        print("The response of ResourcesApi->dataset_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->dataset_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **dataset_uuid** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**GetDatasetResponse**](GetDatasetResponse.md)

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

# **dataset_list**
> List[GetDatasetResponse] dataset_list(uuid, settings=settings)

Get Datasets

Get all datasets for the data source

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_dataset_response import GetDatasetResponse
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
    settings = None # object |  (optional)

    try:
        # Get Datasets
        api_response = api_instance.dataset_list(uuid, settings=settings)
        print("The response of ResourcesApi->dataset_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->dataset_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**List[GetDatasetResponse]**](GetDatasetResponse.md)

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
    api_instance = occam_sdk.ResourcesApi(api_client)
    uuid = 'uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Delete Credential
        api_response = api_instance.delete_credential_credentials_uuid_delete(uuid, settings=settings)
        print("The response of ResourcesApi->delete_credential_credentials_uuid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->delete_credential_credentials_uuid_delete: %s\n" % e)
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

# **resource_add_datasource**
> AddDataSourceResponse resource_add_datasource(add_data_source_request, include_datasets=include_datasets, settings=settings)

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
    settings = None # object |  (optional)

    try:
        # Add Resource
        api_response = api_instance.resource_add_datasource(add_data_source_request, include_datasets=include_datasets, settings=settings)
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
 **settings** | [**object**](.md)|  | [optional] 

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
> GetResourceResponse resource_connect(uuid, add_user_to_resource_request, include_datasets=include_datasets, settings=settings)

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
    uuid = 'uuid_example' # str | 
    add_user_to_resource_request = occam_sdk.AddUserToResourceRequest() # AddUserToResourceRequest | 
    include_datasets = False # bool |  (optional) (default to False)
    settings = None # object |  (optional)

    try:
        # Update User Resource Connection
        api_response = api_instance.resource_connect(uuid, add_user_to_resource_request, include_datasets=include_datasets, settings=settings)
        print("The response of ResourcesApi->resource_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **add_user_to_resource_request** | [**AddUserToResourceRequest**](AddUserToResourceRequest.md)|  | 
 **include_datasets** | **bool**|  | [optional] [default to False]
 **settings** | [**object**](.md)|  | [optional] 

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

Get Datasources Schemas

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
        # Get Datasources Schemas
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
> object resource_delete_connection(resource_connection_deletion_request, settings=settings)

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
    settings = None # object |  (optional)

    try:
        # Delete Connection
        api_response = api_instance.resource_delete_connection(resource_connection_deletion_request, settings=settings)
        print("The response of ResourcesApi->resource_delete_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_delete_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_connection_deletion_request** | [**ResourceConnectionDeletionRequest**](ResourceConnectionDeletionRequest.md)|  | 
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

# **resource_get**
> GetResourceResponse resource_get(uuid, include_datasets=include_datasets, settings=settings)

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
    uuid = 'uuid_example' # str | 
    include_datasets = False # bool |  (optional) (default to False)
    settings = None # object |  (optional)

    try:
        # Get Resource
        api_response = api_instance.resource_get(uuid, include_datasets=include_datasets, settings=settings)
        print("The response of ResourcesApi->resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **include_datasets** | **bool**|  | [optional] [default to False]
 **settings** | [**object**](.md)|  | [optional] 

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

# **resource_get_files**
> Dict[str, ListedKey] resource_get_files(uuid, key=key, settings=settings)

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
    uuid = 'uuid_example' # str | 
    key = 'key_example' # str |  (optional)
    settings = None # object |  (optional)

    try:
        # Get Resource Files
        api_response = api_instance.resource_get_files(uuid, key=key, settings=settings)
        print("The response of ResourcesApi->resource_get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **key** | **str**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 

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

# **resource_list**
> GetResourcesResponse resource_list(include_datasets=include_datasets, settings=settings)

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
    settings = None # object |  (optional)

    try:
        # Get Resources
        api_response = api_instance.resource_list(include_datasets=include_datasets, settings=settings)
        print("The response of ResourcesApi->resource_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_datasets** | **bool**|  | [optional] [default to False]
 **settings** | [**object**](.md)|  | [optional] 

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

# **resource_refresh**
> object resource_refresh(refresh_resources_request, settings=settings)

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
    settings = None # object |  (optional)

    try:
        # Refresh Resources
        api_response = api_instance.resource_refresh(refresh_resources_request, settings=settings)
        print("The response of ResourcesApi->resource_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_resources_request** | [**RefreshResourcesRequest**](RefreshResourcesRequest.md)|  | 
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

# **resource_schema**
> GetResourceSchemaResponse resource_schema(resource_kind, settings=settings)

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
    settings = None # object |  (optional)

    try:
        # Get Resource Schema
        api_response = api_instance.resource_schema(resource_kind, settings=settings)
        print("The response of ResourcesApi->resource_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_kind** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

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

# **resource_tools_schemas**
> List[ResponseResourceInfo] resource_tools_schemas()

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
        api_response = api_instance.resource_tools_schemas()
        print("The response of ResourcesApi->resource_tools_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_tools_schemas: %s\n" % e)
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
> object resource_update(uuid, update_user_resource_request, settings=settings)

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
    uuid = 'uuid_example' # str | 
    update_user_resource_request = occam_sdk.UpdateUserResourceRequest() # UpdateUserResourceRequest | 
    settings = None # object |  (optional)

    try:
        # Update User Resource
        api_response = api_instance.resource_update(uuid, update_user_resource_request, settings=settings)
        print("The response of ResourcesApi->resource_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resource_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **update_user_resource_request** | [**UpdateUserResourceRequest**](UpdateUserResourceRequest.md)|  | 
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
    api_instance = occam_sdk.ResourcesApi(api_client)
    file = None # bytearray | 
    settings = None # object |  (optional)

    try:
        # Upload File
        api_response = api_instance.upload_file_credentials_fileupload_post(file, settings=settings)
        print("The response of ResourcesApi->upload_file_credentials_fileupload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->upload_file_credentials_fileupload_post: %s\n" % e)
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

