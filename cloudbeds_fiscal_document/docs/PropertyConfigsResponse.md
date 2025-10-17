# PropertyConfigsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**Dict[str, ConfigsResponse]**](ConfigsResponse.md) | Map of document kind to fiscal document configuration | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.property_configs_response import PropertyConfigsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyConfigsResponse from a JSON string
property_configs_response_instance = PropertyConfigsResponse.from_json(json)
# print the JSON string representation of the object
print(PropertyConfigsResponse.to_json())

# convert the object into a dict
property_configs_response_dict = property_configs_response_instance.to_dict()
# create an instance of PropertyConfigsResponse from a dict
property_configs_response_from_dict = PropertyConfigsResponse.from_dict(property_configs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


