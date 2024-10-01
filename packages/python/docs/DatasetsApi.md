# occam_sdk.DatasetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataset_add**](DatasetsApi.md#dataset_add) | **POST** /resources/{resource_uuid}/datasets | Batch Add Dataset
[**dataset_allowed_schemas**](DatasetsApi.md#dataset_allowed_schemas) | **GET** /resources/{resource_uuid}/datasets/schema | Get Datasource Dataset Schemas
[**dataset_delete**](DatasetsApi.md#dataset_delete) | **DELETE** /resources/{resource_uuid}/datasets/{dataset_uuid} | Delete Dataset
[**dataset_get**](DatasetsApi.md#dataset_get) | **GET** /resources/{resource_uuid}/datasets/{dataset_uuid} | Get Dataset
[**dataset_list**](DatasetsApi.md#dataset_list) | **GET** /resources/{resource_uuid}/datasets | Get Datasets
[**dataset_update**](DatasetsApi.md#dataset_update) | **POST** /resources/{resource_uuid}/datasets/{dataset_uuid} | Edit Dataset


# **dataset_add**
> List[ResponseBatchAddDataset] dataset_add(resource_uuid, add_dataset_request)

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
    api_instance = occam_sdk.DatasetsApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    add_dataset_request = [occam_sdk.AddDatasetRequest()] # List[AddDatasetRequest] | 

    try:
        # Batch Add Dataset
        api_response = api_instance.dataset_add(resource_uuid, add_dataset_request)
        print("The response of DatasetsApi->dataset_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->dataset_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **add_dataset_request** | [**List[AddDatasetRequest]**](AddDatasetRequest.md)|  | 

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

# **dataset_allowed_schemas**
> ResponseDatasourceDatasetSchemas dataset_allowed_schemas(resource_uuid)

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
    api_instance = occam_sdk.DatasetsApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 

    try:
        # Get Datasource Dataset Schemas
        api_response = api_instance.dataset_allowed_schemas(resource_uuid)
        print("The response of DatasetsApi->dataset_allowed_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->dataset_allowed_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 

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

# **dataset_delete**
> UUIDResponse dataset_delete(resource_uuid, dataset_uuid)

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
    api_instance = occam_sdk.DatasetsApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    dataset_uuid = 'dataset_uuid_example' # str | 

    try:
        # Delete Dataset
        api_response = api_instance.dataset_delete(resource_uuid, dataset_uuid)
        print("The response of DatasetsApi->dataset_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->dataset_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **dataset_uuid** | **str**|  | 

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

# **dataset_get**
> GetDatasetResponse dataset_get(resource_uuid, dataset_uuid)

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
    api_instance = occam_sdk.DatasetsApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    dataset_uuid = 'dataset_uuid_example' # str | 

    try:
        # Get Dataset
        api_response = api_instance.dataset_get(resource_uuid, dataset_uuid)
        print("The response of DatasetsApi->dataset_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->dataset_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **dataset_uuid** | **str**|  | 

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
> List[GetDatasetResponse] dataset_list(resource_uuid)

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
    api_instance = occam_sdk.DatasetsApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 

    try:
        # Get Datasets
        api_response = api_instance.dataset_list(resource_uuid)
        print("The response of DatasetsApi->dataset_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->dataset_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 

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

# **dataset_update**
> EditDatasetResponse dataset_update(resource_uuid, dataset_uuid, edit_dataset_request)

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
    api_instance = occam_sdk.DatasetsApi(api_client)
    resource_uuid = 'resource_uuid_example' # str | 
    dataset_uuid = 'dataset_uuid_example' # str | 
    edit_dataset_request = occam_sdk.EditDatasetRequest() # EditDatasetRequest | 

    try:
        # Edit Dataset
        api_response = api_instance.dataset_update(resource_uuid, dataset_uuid, edit_dataset_request)
        print("The response of DatasetsApi->dataset_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->dataset_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uuid** | **str**|  | 
 **dataset_uuid** | **str**|  | 
 **edit_dataset_request** | [**EditDatasetRequest**](EditDatasetRequest.md)|  | 

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

