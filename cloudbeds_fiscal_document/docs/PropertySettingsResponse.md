# PropertySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_registry** | [**IssuerRegistryResponse**](IssuerRegistryResponse.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.property_settings_response import PropertySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySettingsResponse from a JSON string
property_settings_response_instance = PropertySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PropertySettingsResponse.to_json())

# convert the object into a dict
property_settings_response_dict = property_settings_response_instance.to_dict()
# create an instance of PropertySettingsResponse from a dict
property_settings_response_from_dict = PropertySettingsResponse.from_dict(property_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


