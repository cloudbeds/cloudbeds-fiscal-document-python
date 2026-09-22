# FiscalProviderSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**var_schema** | **Dict[str, object]** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_provider_section import FiscalProviderSection

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalProviderSection from a JSON string
fiscal_provider_section_instance = FiscalProviderSection.from_json(json)
# print the JSON string representation of the object
print(FiscalProviderSection.to_json())

# convert the object into a dict
fiscal_provider_section_dict = fiscal_provider_section_instance.to_dict()
# create an instance of FiscalProviderSection from a dict
fiscal_provider_section_from_dict = FiscalProviderSection.from_dict(fiscal_provider_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


