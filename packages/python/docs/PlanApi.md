# occam_sdk.PlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_goal_plans_goal_post**](PlanApi.md#create_goal_plans_goal_post) | **POST** /plans/goal | Create Goal
[**create_plan_graph_plans_post**](PlanApi.md#create_plan_graph_plans_post) | **POST** /plans | Create Plan Graph
[**get_goal_plans_goal_goal_id_get**](PlanApi.md#get_goal_plans_goal_goal_id_get) | **GET** /plans/goal/{goal_id} | Get Goal
[**get_user_plans_plans_user_user_uuid_get**](PlanApi.md#get_user_plans_plans_user_user_uuid_get) | **GET** /plans/user/{user_uuid} | Get User Plans
[**pause_plan_run_plans_plan_id_run_pause_post**](PlanApi.md#pause_plan_run_plans_plan_id_run_pause_post) | **POST** /plans/{plan_id}/run/pause | Pause Plan Run
[**ping_plans_ping_get**](PlanApi.md#ping_plans_ping_get) | **GET** /plans/ping | Ping
[**plan_generation_detail_plans_plan_id_generation_detail_get**](PlanApi.md#plan_generation_detail_plans_plan_id_generation_detail_get) | **GET** /plans/{plan_id}/generation/detail | Plan Generation Detail
[**plan_generation_status_plans_plan_id_generation_status_get**](PlanApi.md#plan_generation_status_plans_plan_id_generation_status_get) | **GET** /plans/{plan_id}/generation/status | Plan Generation Status
[**plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get**](PlanApi.md#plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get) | **GET** /plans/{plan_id}/run/agent_updates/check | Plan Run Agent Updates Check
[**plan_run_agent_updates_plans_plan_id_run_agent_updates_get**](PlanApi.md#plan_run_agent_updates_plans_plan_id_run_agent_updates_get) | **GET** /plans/{plan_id}/run/agent_updates | Plan Run Agent Updates
[**plan_run_detail_plans_plan_id_run_detail_get**](PlanApi.md#plan_run_detail_plans_plan_id_run_detail_get) | **GET** /plans/{plan_id}/run/detail | Plan Run Detail
[**plan_run_status_plans_plan_id_run_status_get**](PlanApi.md#plan_run_status_plans_plan_id_run_status_get) | **GET** /plans/{plan_id}/run/status | Plan Run Status
[**request_modifications_plans_plan_id_generation_request_modifications_post**](PlanApi.md#request_modifications_plans_plan_id_generation_request_modifications_post) | **POST** /plans/{plan_id}/generation/request_modifications | Request Modifications
[**request_run_modifications_plans_plan_id_run_request_modifications_post**](PlanApi.md#request_run_modifications_plans_plan_id_run_request_modifications_post) | **POST** /plans/{plan_id}/run/request_modifications | Request Run Modifications
[**resume_plan_run_plans_plan_id_run_resume_post**](PlanApi.md#resume_plan_run_plans_plan_id_run_resume_post) | **POST** /plans/{plan_id}/run/resume | Resume Plan Run
[**run_plan_plans_plan_id_run_post**](PlanApi.md#run_plan_plans_plan_id_run_post) | **POST** /plans/{plan_id}/run | Run Plan
[**update_goal_plans_goal_goal_id_update_post**](PlanApi.md#update_goal_plans_goal_goal_id_update_post) | **POST** /plans/goal/{goal_id}/update | Update Goal
[**validate_chat_token_plans_plan_id_chat_validate_chat_token_post**](PlanApi.md#validate_chat_token_plans_plan_id_chat_validate_chat_token_post) | **POST** /plans/{plan_id}/chat/validate_chat_token | Validate Chat Token
[**validate_plan_plans_plan_id_generation_validate_and_save_post**](PlanApi.md#validate_plan_plans_plan_id_generation_validate_and_save_post) | **POST** /plans/{plan_id}/generation/validate_and_save | Validate Plan


# **create_goal_plans_goal_post**
> object create_goal_plans_goal_post(user_uuid, plan_goal, settings=settings)

Create Goal

### Example


```python
import occam_sdk
from occam_sdk.models.plan_goal import PlanGoal
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
    api_instance = occam_sdk.PlanApi(api_client)
    user_uuid = 'user_uuid_example' # str | 
    plan_goal = occam_sdk.PlanGoal() # PlanGoal | 
    settings = None # object |  (optional)

    try:
        # Create Goal
        api_response = api_instance.create_goal_plans_goal_post(user_uuid, plan_goal, settings=settings)
        print("The response of PlanApi->create_goal_plans_goal_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->create_goal_plans_goal_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**|  | 
 **plan_goal** | [**PlanGoal**](PlanGoal.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

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

# **create_plan_graph_plans_post**
> object create_plan_graph_plans_post(goal_id, user_uuid, settings=settings)

Create Plan Graph

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
    api_instance = occam_sdk.PlanApi(api_client)
    goal_id = 'goal_id_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Create Plan Graph
        api_response = api_instance.create_plan_graph_plans_post(goal_id, user_uuid, settings=settings)
        print("The response of PlanApi->create_plan_graph_plans_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->create_plan_graph_plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **user_uuid** | **str**|  | 
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

# **get_goal_plans_goal_goal_id_get**
> object get_goal_plans_goal_goal_id_get(goal_id)

Get Goal

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
    api_instance = occam_sdk.PlanApi(api_client)
    goal_id = 'goal_id_example' # str | 

    try:
        # Get Goal
        api_response = api_instance.get_goal_plans_goal_goal_id_get(goal_id)
        print("The response of PlanApi->get_goal_plans_goal_goal_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->get_goal_plans_goal_goal_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

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

# **get_user_plans_plans_user_user_uuid_get**
> List[GetUserPlanResponse] get_user_plans_plans_user_user_uuid_get(user_uuid, settings=settings)

Get User Plans

### Example


```python
import occam_sdk
from occam_sdk.models.get_user_plan_response import GetUserPlanResponse
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
    api_instance = occam_sdk.PlanApi(api_client)
    user_uuid = 'user_uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Get User Plans
        api_response = api_instance.get_user_plans_plans_user_user_uuid_get(user_uuid, settings=settings)
        print("The response of PlanApi->get_user_plans_plans_user_user_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->get_user_plans_plans_user_user_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**List[GetUserPlanResponse]**](GetUserPlanResponse.md)

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

# **pause_plan_run_plans_plan_id_run_pause_post**
> object pause_plan_run_plans_plan_id_run_pause_post(plan_id)

Pause Plan Run

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Pause Plan Run
        api_response = api_instance.pause_plan_run_plans_plan_id_run_pause_post(plan_id)
        print("The response of PlanApi->pause_plan_run_plans_plan_id_run_pause_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->pause_plan_run_plans_plan_id_run_pause_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **ping_plans_ping_get**
> object ping_plans_ping_get()

Ping

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
    api_instance = occam_sdk.PlanApi(api_client)

    try:
        # Ping
        api_response = api_instance.ping_plans_ping_get()
        print("The response of PlanApi->ping_plans_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->ping_plans_ping_get: %s\n" % e)
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

# **plan_generation_detail_plans_plan_id_generation_detail_get**
> object plan_generation_detail_plans_plan_id_generation_detail_get(plan_id)

Plan Generation Detail

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Plan Generation Detail
        api_response = api_instance.plan_generation_detail_plans_plan_id_generation_detail_get(plan_id)
        print("The response of PlanApi->plan_generation_detail_plans_plan_id_generation_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_generation_detail_plans_plan_id_generation_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **plan_generation_status_plans_plan_id_generation_status_get**
> object plan_generation_status_plans_plan_id_generation_status_get(plan_id)

Plan Generation Status

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Plan Generation Status
        api_response = api_instance.plan_generation_status_plans_plan_id_generation_status_get(plan_id)
        print("The response of PlanApi->plan_generation_status_plans_plan_id_generation_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_generation_status_plans_plan_id_generation_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get**
> object plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get(plan_id, since=since)

Plan Run Agent Updates Check

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Plan Run Agent Updates Check
        api_response = api_instance.plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get(plan_id, since=since)
        print("The response of PlanApi->plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_run_agent_updates_check_plans_plan_id_run_agent_updates_check_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

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

# **plan_run_agent_updates_plans_plan_id_run_agent_updates_get**
> object plan_run_agent_updates_plans_plan_id_run_agent_updates_get(plan_id, since=since)

Plan Run Agent Updates

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Plan Run Agent Updates
        api_response = api_instance.plan_run_agent_updates_plans_plan_id_run_agent_updates_get(plan_id, since=since)
        print("The response of PlanApi->plan_run_agent_updates_plans_plan_id_run_agent_updates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_run_agent_updates_plans_plan_id_run_agent_updates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

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

# **plan_run_detail_plans_plan_id_run_detail_get**
> object plan_run_detail_plans_plan_id_run_detail_get(plan_id)

Plan Run Detail

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Plan Run Detail
        api_response = api_instance.plan_run_detail_plans_plan_id_run_detail_get(plan_id)
        print("The response of PlanApi->plan_run_detail_plans_plan_id_run_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_run_detail_plans_plan_id_run_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **plan_run_status_plans_plan_id_run_status_get**
> object plan_run_status_plans_plan_id_run_status_get(plan_id)

Plan Run Status

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Plan Run Status
        api_response = api_instance.plan_run_status_plans_plan_id_run_status_get(plan_id)
        print("The response of PlanApi->plan_run_status_plans_plan_id_run_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_run_status_plans_plan_id_run_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **request_modifications_plans_plan_id_generation_request_modifications_post**
> object request_modifications_plans_plan_id_generation_request_modifications_post(plan_id, user_uuid, request_agent_modifications_model, settings=settings)

Request Modifications

### Example


```python
import occam_sdk
from occam_sdk.models.request_agent_modifications_model import RequestAgentModificationsModel
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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    request_agent_modifications_model = occam_sdk.RequestAgentModificationsModel() # RequestAgentModificationsModel | 
    settings = None # object |  (optional)

    try:
        # Request Modifications
        api_response = api_instance.request_modifications_plans_plan_id_generation_request_modifications_post(plan_id, user_uuid, request_agent_modifications_model, settings=settings)
        print("The response of PlanApi->request_modifications_plans_plan_id_generation_request_modifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->request_modifications_plans_plan_id_generation_request_modifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **user_uuid** | **str**|  | 
 **request_agent_modifications_model** | [**RequestAgentModificationsModel**](RequestAgentModificationsModel.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

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

# **request_run_modifications_plans_plan_id_run_request_modifications_post**
> object request_run_modifications_plans_plan_id_run_request_modifications_post(plan_id, user_uuid, user_message_model, settings=settings)

Request Run Modifications

### Example


```python
import occam_sdk
from occam_sdk.models.user_message_model import UserMessageModel
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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    user_message_model = occam_sdk.UserMessageModel() # UserMessageModel | 
    settings = None # object |  (optional)

    try:
        # Request Run Modifications
        api_response = api_instance.request_run_modifications_plans_plan_id_run_request_modifications_post(plan_id, user_uuid, user_message_model, settings=settings)
        print("The response of PlanApi->request_run_modifications_plans_plan_id_run_request_modifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->request_run_modifications_plans_plan_id_run_request_modifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **user_uuid** | **str**|  | 
 **user_message_model** | [**UserMessageModel**](UserMessageModel.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

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

# **resume_plan_run_plans_plan_id_run_resume_post**
> object resume_plan_run_plans_plan_id_run_resume_post(plan_id)

Resume Plan Run

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Resume Plan Run
        api_response = api_instance.resume_plan_run_plans_plan_id_run_resume_post(plan_id)
        print("The response of PlanApi->resume_plan_run_plans_plan_id_run_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->resume_plan_run_plans_plan_id_run_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **run_plan_plans_plan_id_run_post**
> object run_plan_plans_plan_id_run_post(plan_id, user_uuid, settings=settings)

Run Plan

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Run Plan
        api_response = api_instance.run_plan_plans_plan_id_run_post(plan_id, user_uuid, settings=settings)
        print("The response of PlanApi->run_plan_plans_plan_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->run_plan_plans_plan_id_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **user_uuid** | **str**|  | 
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

# **update_goal_plans_goal_goal_id_update_post**
> object update_goal_plans_goal_goal_id_update_post(goal_id, user_uuid, plan_goal, settings=settings)

Update Goal

### Example


```python
import occam_sdk
from occam_sdk.models.plan_goal import PlanGoal
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
    api_instance = occam_sdk.PlanApi(api_client)
    goal_id = 'goal_id_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    plan_goal = occam_sdk.PlanGoal() # PlanGoal | 
    settings = None # object |  (optional)

    try:
        # Update Goal
        api_response = api_instance.update_goal_plans_goal_goal_id_update_post(goal_id, user_uuid, plan_goal, settings=settings)
        print("The response of PlanApi->update_goal_plans_goal_goal_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->update_goal_plans_goal_goal_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **user_uuid** | **str**|  | 
 **plan_goal** | [**PlanGoal**](PlanGoal.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

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

# **validate_chat_token_plans_plan_id_chat_validate_chat_token_post**
> object validate_chat_token_plans_plan_id_chat_validate_chat_token_post(plan_id, chat_channel_id, token, user_uuid, settings=settings)

Validate Chat Token

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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    chat_channel_id = 'chat_channel_id_example' # str | 
    token = 'token_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    settings = None # object |  (optional)

    try:
        # Validate Chat Token
        api_response = api_instance.validate_chat_token_plans_plan_id_chat_validate_chat_token_post(plan_id, chat_channel_id, token, user_uuid, settings=settings)
        print("The response of PlanApi->validate_chat_token_plans_plan_id_chat_validate_chat_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->validate_chat_token_plans_plan_id_chat_validate_chat_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **chat_channel_id** | **str**|  | 
 **token** | **str**|  | 
 **user_uuid** | **str**|  | 
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

# **validate_plan_plans_plan_id_generation_validate_and_save_post**
> object validate_plan_plans_plan_id_generation_validate_and_save_post(plan_id, user_uuid, modifications_batch, settings=settings)

Validate Plan

### Example


```python
import occam_sdk
from occam_sdk.models.modifications_batch import ModificationsBatch
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
    api_instance = occam_sdk.PlanApi(api_client)
    plan_id = 'plan_id_example' # str | 
    user_uuid = 'user_uuid_example' # str | 
    modifications_batch = occam_sdk.ModificationsBatch() # ModificationsBatch | 
    settings = None # object |  (optional)

    try:
        # Validate Plan
        api_response = api_instance.validate_plan_plans_plan_id_generation_validate_and_save_post(plan_id, user_uuid, modifications_batch, settings=settings)
        print("The response of PlanApi->validate_plan_plans_plan_id_generation_validate_and_save_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->validate_plan_plans_plan_id_generation_validate_and_save_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **user_uuid** | **str**|  | 
 **modifications_batch** | [**ModificationsBatch**](ModificationsBatch.md)|  | 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

**object**

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

