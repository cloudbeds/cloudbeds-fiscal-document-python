# PropertySettingsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_registry** | [**IssuerRegistryUpdate**](IssuerRegistryUpdate.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.property_settings_update_request import PropertySettingsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySettingsUpdateRequest from a JSON string
property_settings_update_request_instance = PropertySettingsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PropertySettingsUpdateRequest.to_json())

# convert the object into a dict
property_settings_update_request_dict = property_settings_update_request_instance.to_dict()
# create an instance of PropertySettingsUpdateRequest from a dict
property_settings_update_request_from_dict = PropertySettingsUpdateRequest.from_dict(property_settings_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


