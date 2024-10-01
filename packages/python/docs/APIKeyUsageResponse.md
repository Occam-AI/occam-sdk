# APIKeyUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_requests** | **int** |  | 
**successful_requests** | **int** |  | 
**failed_requests** | **int** |  | 
**quota_usage_percentage** | **float** |  | 
**requests_per_day** | **float** |  | 

## Example

```python
from occam_sdk.models.api_key_usage_response import APIKeyUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyUsageResponse from a JSON string
api_key_usage_response_instance = APIKeyUsageResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyUsageResponse.to_json())

# convert the object into a dict
api_key_usage_response_dict = api_key_usage_response_instance.to_dict()
# create an instance of APIKeyUsageResponse from a dict
api_key_usage_response_from_dict = APIKeyUsageResponse.from_dict(api_key_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


