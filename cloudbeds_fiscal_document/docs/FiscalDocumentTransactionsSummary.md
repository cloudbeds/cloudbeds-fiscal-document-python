# FiscalDocumentTransactionsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges_and_adjustments** | **str** |  | [optional] 
**taxes** | [**List[FiscalDocumentTransactionsSummaryTaxesInner]**](FiscalDocumentTransactionsSummaryTaxesInner.md) |  | [optional] 
**paid** | **str** |  | [optional] 
**refunded** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**currency** | **str** | Currency the totals are expressed in. Equals the requested invoice currency when one was provided (totals converted from the property currency using the property&#39;s configured exchange rates), otherwise the property currency. | [optional] 
**property_currency** | **str** | The property&#39;s base currency code. | [optional] 
**property_currency_total** | **str** | The invoice total in the property&#39;s base currency, shown as a reference alongside the converted total when an invoice currency was requested. | [optional] 
**transaction_count** | **int** | Number of transactions the current selection resolves to. Lets the caller warn before submitting a selection that would be rejected for exceeding maxTransactions. | [optional] 
**max_transactions** | **int** | Maximum number of transactions allowed on a single fiscal document. | [optional] 

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


