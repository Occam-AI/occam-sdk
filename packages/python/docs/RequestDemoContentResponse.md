# RequestDemoContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | 
**job_function** | **str** |  | 
**use_case** | **str** |  | 
**company_name** | **str** |  | 
**company_size_range** | **str** |  | 
**linkedin_url** | **str** |  | [optional] 

## Example

```python
from occam_sdk.models.request_demo_content_response import RequestDemoContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDemoContentResponse from a JSON string
request_demo_content_response_instance = RequestDemoContentResponse.from_json(json)
# print the JSON string representation of the object
print(RequestDemoContentResponse.to_json())

# convert the object into a dict
request_demo_content_response_dict = request_demo_content_response_instance.to_dict()
# create an instance of RequestDemoContentResponse from a dict
request_demo_content_response_from_dict = RequestDemoContentResponse.from_dict(request_demo_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


