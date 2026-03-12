# FiscalizationTaxRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryInfo**](CountryInfo.md) |  | 
**taxes** | [**List[TaxRule]**](TaxRule.md) | Flat list of selectable tax category + rate combinations | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_tax_rules_response import FiscalizationTaxRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationTaxRulesResponse from a JSON string
fiscalization_tax_rules_response_instance = FiscalizationTaxRulesResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationTaxRulesResponse.to_json())

# convert the object into a dict
fiscalization_tax_rules_response_dict = fiscalization_tax_rules_response_instance.to_dict()
# create an instance of FiscalizationTaxRulesResponse from a dict
fiscalization_tax_rules_response_from_dict = FiscalizationTaxRulesResponse.from_dict(fiscalization_tax_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


