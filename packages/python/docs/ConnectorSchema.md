# ConnectorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**var_schema** | **object** |  | [optional] 

## Example

```python
from occam_sdk.models.connector_schema import ConnectorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorSchema from a JSON string
connector_schema_instance = ConnectorSchema.from_json(json)
# print the JSON string representation of the object
print(ConnectorSchema.to_json())

# convert the object into a dict
connector_schema_dict = connector_schema_instance.to_dict()
# create an instance of ConnectorSchema from a dict
connector_schema_from_dict = ConnectorSchema.from_dict(connector_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


