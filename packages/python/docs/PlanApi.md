# occam_sdk.PlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_goal_plans_goal_post**](PlanApi.md#create_goal_plans_goal_post) | **POST** /plans/goal | Create Goal
[**create_plan_graph_plans_post**](PlanApi.md#create_plan_graph_plans_post) | **POST** /plans | Create Plan Graph
[**get_goal_plans_goal_goal_id_get**](PlanApi.md#get_goal_plans_goal_goal_id_get) | **GET** /plans/goal/{goal_id} | Get Goal
[**get_user_plans_plans_user_user_uuid_get**](PlanApi.md#get_user_plans_plans_user_user_uuid_get) | **GET** /plans/user/{user_uuid} | Get User Plans
[**modify_plan_plans_plan_id_modify_post**](PlanApi.md#modify_plan_plans_plan_id_modify_post) | **POST** /plans/{plan_id}/modify | Modify Plan
[**ping_plans_ping_get**](PlanApi.md#ping_plans_ping_get) | **GET** /plans/ping | Ping
[**plan_status_plans_plan_id_status_get**](PlanApi.md#plan_status_plans_plan_id_status_get) | **GET** /plans/{plan_id}/status | Plan Status
[**run_plan_plans_plan_id_run_post**](PlanApi.md#run_plan_plans_plan_id_run_post) | **POST** /plans/{plan_id}/run | Run Plan
[**simulate_plan_plans_plan_id_test_post**](PlanApi.md#simulate_plan_plans_plan_id_test_post) | **POST** /plans/{plan_id}/test | Simulate Plan
[**update_goal_plans_goal_goal_id_update_post**](PlanApi.md#update_goal_plans_goal_goal_id_update_post) | **POST** /plans/goal/{goal_id}/update | Update Goal


# **create_goal_plans_goal_post**
> object create_goal_plans_goal_post(user_uuid, plan_goal)

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

    try:
        # Create Goal
        api_response = api_instance.create_goal_plans_goal_post(user_uuid, plan_goal)
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
> object create_plan_graph_plans_post(goal_id, user_uuid)

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

    try:
        # Create Plan Graph
        api_response = api_instance.create_plan_graph_plans_post(goal_id, user_uuid)
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
> List[GetUserPlanResponse] get_user_plans_plans_user_user_uuid_get(user_uuid)

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

    try:
        # Get User Plans
        api_response = api_instance.get_user_plans_plans_user_user_uuid_get(user_uuid)
        print("The response of PlanApi->get_user_plans_plans_user_user_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->get_user_plans_plans_user_user_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**|  | 

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

# **modify_plan_plans_plan_id_modify_post**
> object modify_plan_plans_plan_id_modify_post(plan_id)

Modify Plan

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
        # Modify Plan
        api_response = api_instance.modify_plan_plans_plan_id_modify_post(plan_id)
        print("The response of PlanApi->modify_plan_plans_plan_id_modify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->modify_plan_plans_plan_id_modify_post: %s\n" % e)
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

# **plan_status_plans_plan_id_status_get**
> object plan_status_plans_plan_id_status_get(plan_id, detail=detail)

Plan Status

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
    detail = occam_sdk.PlanStatusDetail() # PlanStatusDetail |  (optional)

    try:
        # Plan Status
        api_response = api_instance.plan_status_plans_plan_id_status_get(plan_id, detail=detail)
        print("The response of PlanApi->plan_status_plans_plan_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->plan_status_plans_plan_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **detail** | [**PlanStatusDetail**](.md)|  | [optional] 

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
> object run_plan_plans_plan_id_run_post(plan_id)

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

    try:
        # Run Plan
        api_response = api_instance.run_plan_plans_plan_id_run_post(plan_id)
        print("The response of PlanApi->run_plan_plans_plan_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->run_plan_plans_plan_id_run_post: %s\n" % e)
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

# **simulate_plan_plans_plan_id_test_post**
> object simulate_plan_plans_plan_id_test_post(plan_id, plan_simulation_params)

Simulate Plan

### Example


```python
import occam_sdk
from occam_sdk.models.plan_simulation_params import PlanSimulationParams
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
    plan_simulation_params = occam_sdk.PlanSimulationParams() # PlanSimulationParams | 

    try:
        # Simulate Plan
        api_response = api_instance.simulate_plan_plans_plan_id_test_post(plan_id, plan_simulation_params)
        print("The response of PlanApi->simulate_plan_plans_plan_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->simulate_plan_plans_plan_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **plan_simulation_params** | [**PlanSimulationParams**](PlanSimulationParams.md)|  | 

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

# **update_goal_plans_goal_goal_id_update_post**
> object update_goal_plans_goal_goal_id_update_post(goal_id, user_uuid, plan_goal)

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

    try:
        # Update Goal
        api_response = api_instance.update_goal_plans_goal_goal_id_update_post(goal_id, user_uuid, plan_goal)
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

