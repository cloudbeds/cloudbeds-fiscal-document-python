# FiscalizationTaxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxes** | [**List[TaxMapping]**](TaxMapping.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_tax_request import FiscalizationTaxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationTaxRequest from a JSON string
fiscalization_tax_request_instance = FiscalizationTaxRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalizationTaxRequest.to_json())

# convert the object into a dict
fiscalization_tax_request_dict = fiscalization_tax_request_instance.to_dict()
# create an instance of FiscalizationTaxRequest from a dict
fiscalization_tax_request_from_dict = FiscalizationTaxRequest.from_dict(fiscalization_tax_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


