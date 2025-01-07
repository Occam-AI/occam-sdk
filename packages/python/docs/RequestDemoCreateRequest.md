# RequestDemoCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | 
**linkedin_url** | **str** |  | [optional] 
**job_function** | **str** |  | 
**use_case** | **str** |  | 
**company_name** | **str** |  | 
**company_size_range** | **str** |  | 

## Example

```python
from occam_sdk.models.request_demo_create_request import RequestDemoCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDemoCreateRequest from a JSON string
request_demo_create_request_instance = RequestDemoCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RequestDemoCreateRequest.to_json())

# convert the object into a dict
request_demo_create_request_dict = request_demo_create_request_instance.to_dict()
# create an instance of RequestDemoCreateRequest from a dict
request_demo_create_request_from_dict = RequestDemoCreateRequest.from_dict(request_demo_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


