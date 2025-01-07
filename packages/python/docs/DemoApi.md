# occam_sdk.DemoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_demo_demo_request_uuid_get**](DemoApi.md#get_demo_demo_request_uuid_get) | **GET** /demo/request/{uuid} | Get Demo
[**list_demo_demo_list_get**](DemoApi.md#list_demo_demo_list_get) | **GET** /demo/list | List Demo
[**request_demo_demo_request_post**](DemoApi.md#request_demo_demo_request_post) | **POST** /demo/request | Request Demo


# **get_demo_demo_request_uuid_get**
> RequestDemoContentResponse get_demo_demo_request_uuid_get(uuid, settings=settings)

Get Demo

### Example


```python
import occam_sdk
from occam_sdk.models.request_demo_content_response import RequestDemoContentResponse
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
    api_instance = occam_sdk.DemoApi(api_client)
    uuid = 'uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Get Demo
        api_response = api_instance.get_demo_demo_request_uuid_get(uuid, settings=settings)
        print("The response of DemoApi->get_demo_demo_request_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->get_demo_demo_request_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**RequestDemoContentResponse**](RequestDemoContentResponse.md)

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

# **list_demo_demo_list_get**
> List[RequestDemoResponse] list_demo_demo_list_get(settings=settings)

List Demo

### Example


```python
import occam_sdk
from occam_sdk.models.request_demo_response import RequestDemoResponse
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
    api_instance = occam_sdk.DemoApi(api_client)
    settings = None # object |  (optional)

    try:
        # List Demo
        api_response = api_instance.list_demo_demo_list_get(settings=settings)
        print("The response of DemoApi->list_demo_demo_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->list_demo_demo_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**List[RequestDemoResponse]**](RequestDemoResponse.md)

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

# **request_demo_demo_request_post**
> RequestDemoResponse request_demo_demo_request_post(request_demo_create_request, settings=settings)

Request Demo

### Example


```python
import occam_sdk
from occam_sdk.models.request_demo_create_request import RequestDemoCreateRequest
from occam_sdk.models.request_demo_response import RequestDemoResponse
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
    api_instance = occam_sdk.DemoApi(api_client)
    request_demo_create_request = occam_sdk.RequestDemoCreateRequest() # RequestDemoCreateRequest | 
    settings = None # object |  (optional)

    try:
        # Request Demo
        api_response = api_instance.request_demo_demo_request_post(request_demo_create_request, settings=settings)
        print("The response of DemoApi->request_demo_demo_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->request_demo_demo_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_demo_create_request** | [**RequestDemoCreateRequest**](RequestDemoCreateRequest.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**RequestDemoResponse**](RequestDemoResponse.md)

### Authorization

No authorization required

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

