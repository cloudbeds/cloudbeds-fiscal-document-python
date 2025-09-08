# FiscalDocumentTransactionsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges_and_adjustments** | **str** |  | [optional] 
**taxes** | [**List[FiscalDocumentTransactionsSummaryTaxesInner]**](FiscalDocumentTransactionsSummaryTaxesInner.md) |  | [optional] 
**paid** | **str** |  | [optional] 
**refunded** | **str** |  | [optional] 
**total** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_transactions_summary import FiscalDocumentTransactionsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentTransactionsSummary from a JSON string
fiscal_document_transactions_summary_instance = FiscalDocumentTransactionsSummary.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentTransactionsSummary.to_json())

# convert the object into a dict
fiscal_document_transactions_summary_dict = fiscal_document_transactions_summary_instance.to_dict()
# create an instance of FiscalDocumentTransactionsSummary from a dict
fiscal_document_transactions_summary_from_dict = FiscalDocumentTransactionsSummary.from_dict(fiscal_document_transactions_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


