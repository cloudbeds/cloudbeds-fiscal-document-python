# FiscalizationProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | Name of the fiscalization provider (e.g., Invopop, Fonoa, Fiskaly) | 
**country_code** | **str** | ISO 3166-1 alpha-2 country code | 
**country_name** | **str** | Human-readable country name | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_provider_info import FiscalizationProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationProviderInfo from a JSON string
fiscalization_provider_info_instance = FiscalizationProviderInfo.from_json(json)
# print the JSON string representation of the object
print(FiscalizationProviderInfo.to_json())

# convert the object into a dict
fiscalization_provider_info_dict = fiscalization_provider_info_instance.to_dict()
# create an instance of FiscalizationProviderInfo from a dict
fiscalization_provider_info_from_dict = FiscalizationProviderInfo.from_dict(fiscalization_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


