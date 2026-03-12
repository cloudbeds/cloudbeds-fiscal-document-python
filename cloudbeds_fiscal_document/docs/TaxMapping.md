# TaxMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** | Tax ID from the accounting system | 
**category** | **str** | Tax category code (e.g., VAT, ISR) | 
**key** | **str** | Tax key describing the tax situation (e.g., standard, exempt) | 
**rate** | **str** | Rate within the category and key (e.g., general, reduced) | 

## Example

```python
from cloudbeds_fiscal_document.models.tax_mapping import TaxMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TaxMapping from a JSON string
tax_mapping_instance = TaxMapping.from_json(json)
# print the JSON string representation of the object
print(TaxMapping.to_json())

# convert the object into a dict
tax_mapping_dict = tax_mapping_instance.to_dict()
# create an instance of TaxMapping from a dict
tax_mapping_from_dict = TaxMapping.from_dict(tax_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


