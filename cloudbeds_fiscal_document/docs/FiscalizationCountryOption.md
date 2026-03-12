# FiscalizationCountryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISO 3166-1 alpha-2 country code | 
**name** | **str** | Country name | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_country_option import FiscalizationCountryOption

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationCountryOption from a JSON string
fiscalization_country_option_instance = FiscalizationCountryOption.from_json(json)
# print the JSON string representation of the object
print(FiscalizationCountryOption.to_json())

# convert the object into a dict
fiscalization_country_option_dict = fiscalization_country_option_instance.to_dict()
# create an instance of FiscalizationCountryOption from a dict
fiscalization_country_option_from_dict = FiscalizationCountryOption.from_dict(fiscalization_country_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


