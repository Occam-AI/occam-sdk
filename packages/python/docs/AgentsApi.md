# occam_sdk.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_agents_agent_name_create_post**](AgentsApi.md#create_agent_agents_agent_name_create_post) | **POST** /agents/{agent_name}/create | Create Agent
[**get_agent_agents_agent_name_get**](AgentsApi.md#get_agent_agents_agent_name_get) | **GET** /agents/{agent_name} | Get Agent
[**get_agent_run_status_agents_agent_run_instance_id_status_get**](AgentsApi.md#get_agent_run_status_agents_agent_run_instance_id_status_get) | **GET** /agents/{agent_run_instance_id}/status | Get Agent Run Status
[**list_agents_agents_get**](AgentsApi.md#list_agents_agents_get) | **GET** /agents/ | List Agents
[**run_agent_agents_agent_instance_id_run_post**](AgentsApi.md#run_agent_agents_agent_instance_id_run_post) | **POST** /agents/{agent_instance_id}/run | Run Agent


# **create_agent_agents_agent_name_create_post**
> CreateAgentResponse create_agent_agents_agent_name_create_post(agent_name, create_agent_request, operation_id=operation_id, settings=settings)

Create Agent

Create an instance of anagent

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.create_agent_request import CreateAgentRequest
from occam_sdk.models.create_agent_response import CreateAgentResponse
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
    api_instance = occam_sdk.AgentsApi(api_client)
    agent_name = 'agent_name_example' # str | 
    create_agent_request = occam_sdk.CreateAgentRequest() # CreateAgentRequest | 
    operation_id = 'create_agent' # str |  (optional) (default to 'create_agent')
    settings = None # object |  (optional)

    try:
        # Create Agent
        api_response = api_instance.create_agent_agents_agent_name_create_post(agent_name, create_agent_request, operation_id=operation_id, settings=settings)
        print("The response of AgentsApi->create_agent_agents_agent_name_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_agents_agent_name_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_name** | **str**|  | 
 **create_agent_request** | [**CreateAgentRequest**](CreateAgentRequest.md)|  | 
 **operation_id** | **str**|  | [optional] [default to &#39;create_agent&#39;]
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**CreateAgentResponse**](CreateAgentResponse.md)

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

# **get_agent_agents_agent_name_get**
> AgentIdentityResponse get_agent_agents_agent_name_get(agent_name, operation_id=operation_id, settings=settings)

Get Agent

Get an agent by name

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.agent_identity_response import AgentIdentityResponse
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
    api_instance = occam_sdk.AgentsApi(api_client)
    agent_name = 'agent_name_example' # str | 
    operation_id = 'get_agent' # str |  (optional) (default to 'get_agent')
    settings = None # object |  (optional)

    try:
        # Get Agent
        api_response = api_instance.get_agent_agents_agent_name_get(agent_name, operation_id=operation_id, settings=settings)
        print("The response of AgentsApi->get_agent_agents_agent_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_agents_agent_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_name** | **str**|  | 
 **operation_id** | **str**|  | [optional] [default to &#39;get_agent&#39;]
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**AgentIdentityResponse**](AgentIdentityResponse.md)

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

# **get_agent_run_status_agents_agent_run_instance_id_status_get**
> GetAgentRunStatusResponse get_agent_run_status_agents_agent_run_instance_id_status_get(agent_run_instance_id, operation_id=operation_id, settings=settings)

Get Agent Run Status

Get the status of an agent run given an instance ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.get_agent_run_status_response import GetAgentRunStatusResponse
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
    api_instance = occam_sdk.AgentsApi(api_client)
    agent_run_instance_id = 'agent_run_instance_id_example' # str | 
    operation_id = 'get_agent_run_status' # str |  (optional) (default to 'get_agent_run_status')
    settings = None # object |  (optional)

    try:
        # Get Agent Run Status
        api_response = api_instance.get_agent_run_status_agents_agent_run_instance_id_status_get(agent_run_instance_id, operation_id=operation_id, settings=settings)
        print("The response of AgentsApi->get_agent_run_status_agents_agent_run_instance_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_run_status_agents_agent_run_instance_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_instance_id** | **str**|  | 
 **operation_id** | **str**|  | [optional] [default to &#39;get_agent_run_status&#39;]
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**GetAgentRunStatusResponse**](GetAgentRunStatusResponse.md)

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

# **list_agents_agents_get**
> List[AgentIdentityResponse] list_agents_agents_get(operation_id=operation_id, settings=settings)

List Agents

List all available agents for the calling user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.agent_identity_response import AgentIdentityResponse
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
    api_instance = occam_sdk.AgentsApi(api_client)
    operation_id = 'list_agents' # str |  (optional) (default to 'list_agents')
    settings = None # object |  (optional)

    try:
        # List Agents
        api_response = api_instance.list_agents_agents_get(operation_id=operation_id, settings=settings)
        print("The response of AgentsApi->list_agents_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agents_agents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**|  | [optional] [default to &#39;list_agents&#39;]
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**List[AgentIdentityResponse]**](AgentIdentityResponse.md)

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

# **run_agent_agents_agent_instance_id_run_post**
> RunAgentResponse run_agent_agents_agent_instance_id_run_post(agent_instance_id, run_agent_request, operation_id=operation_id, settings=settings)

Run Agent

Run an agent given an instance ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import occam_sdk
from occam_sdk.models.run_agent_request import RunAgentRequest
from occam_sdk.models.run_agent_response import RunAgentResponse
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
    api_instance = occam_sdk.AgentsApi(api_client)
    agent_instance_id = 'agent_instance_id_example' # str | 
    run_agent_request = occam_sdk.RunAgentRequest() # RunAgentRequest | 
    operation_id = 'run_agent' # str |  (optional) (default to 'run_agent')
    settings = None # object |  (optional)

    try:
        # Run Agent
        api_response = api_instance.run_agent_agents_agent_instance_id_run_post(agent_instance_id, run_agent_request, operation_id=operation_id, settings=settings)
        print("The response of AgentsApi->run_agent_agents_agent_instance_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->run_agent_agents_agent_instance_id_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_instance_id** | **str**|  | 
 **run_agent_request** | [**RunAgentRequest**](RunAgentRequest.md)|  | 
 **operation_id** | **str**|  | [optional] [default to &#39;run_agent&#39;]
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**RunAgentResponse**](RunAgentResponse.md)

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

