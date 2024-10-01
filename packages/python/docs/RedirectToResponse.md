# RedirectToResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from occam_sdk.models.redirect_to_response import RedirectToResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectToResponse from a JSON string
redirect_to_response_instance = RedirectToResponse.from_json(json)
# print the JSON string representation of the object
print(RedirectToResponse.to_json())

# convert the object into a dict
redirect_to_response_dict = redirect_to_response_instance.to_dict()
# create an instance of RedirectToResponse from a dict
redirect_to_response_from_dict = RedirectToResponse.from_dict(redirect_to_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


