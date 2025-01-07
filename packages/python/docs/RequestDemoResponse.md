# RequestDemoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from occam_sdk.models.request_demo_response import RequestDemoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDemoResponse from a JSON string
request_demo_response_instance = RequestDemoResponse.from_json(json)
# print the JSON string representation of the object
print(RequestDemoResponse.to_json())

# convert the object into a dict
request_demo_response_dict = request_demo_response_instance.to_dict()
# create an instance of RequestDemoResponse from a dict
request_demo_response_from_dict = RequestDemoResponse.from_dict(request_demo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


