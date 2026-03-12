# TaxRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Tax category code (e.g., VAT, ISR) | 
**key** | **str** | Tax key describing the tax situation (e.g., standard, exempt) | 
**rate** | **str** | Rate within the category and key (e.g., general, reduced) | 
**name** | **str** | Display name (e.g., \&quot;VAT - General Rate (16.0%)\&quot;) | 
**percent** | **str** | Rate percentage (e.g., \&quot;16.0%\&quot;) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.tax_rule import TaxRule

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRule from a JSON string
tax_rule_instance = TaxRule.from_json(json)
# print the JSON string representation of the object
print(TaxRule.to_json())

# convert the object into a dict
tax_rule_dict = tax_rule_instance.to_dict()
# create an instance of TaxRule from a dict
tax_rule_from_dict = TaxRule.from_dict(tax_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


