# FiscalizationTaxResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxes** | [**List[TaxMapping]**](TaxMapping.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_tax_response import FiscalizationTaxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationTaxResponse from a JSON string
fiscalization_tax_response_instance = FiscalizationTaxResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationTaxResponse.to_json())

# convert the object into a dict
fiscalization_tax_response_dict = fiscalization_tax_response_instance.to_dict()
# create an instance of FiscalizationTaxResponse from a dict
fiscalization_tax_response_from_dict = FiscalizationTaxResponse.from_dict(fiscalization_tax_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


