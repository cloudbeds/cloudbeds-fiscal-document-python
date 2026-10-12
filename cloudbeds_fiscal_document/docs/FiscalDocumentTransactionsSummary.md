# FiscalDocumentTransactionsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges_and_adjustments** | **str** |  | [optional] 
**taxes** | [**List[FiscalDocumentTransactionsSummaryTaxesInner]**](FiscalDocumentTransactionsSummaryTaxesInner.md) |  | [optional] 
**paid** | **str** |  | [optional] 
**refunded** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**currency** | **str** | Currency the totals are expressed in. For an existing document, the currency it was issued in; for a selection, the requested invoice currency (converted at the property&#39;s configured rates), otherwise the property currency. | [optional] 
**property_currency** | **str** | The property&#39;s base currency code. | [optional] 
**property_currency_total** | **str** | The total in the property&#39;s base currency, shown as a reference alongside the total when the totals are expressed in another currency. | [optional] 
**exchange_rate** | **str** | The property&#39;s configured rate from its base currency into the currency the totals are expressed in (1 base unit &#x3D; exchangeRate units), the rate an invoice issued now is locked at. Absent when the totals are in the property currency or no rate is configured. | [optional] 
**transaction_count** | **int** | Number of transactions the current selection resolves to. Lets the caller warn before submitting a selection that would be rejected for exceeding maxTransactions. | [optional] 
**max_transactions** | **int** | Maximum number of transactions allowed on a single fiscal document. | [optional] 
**replaced_receipts** | **List[str]** | For an invoice selection on a property whose invoice replaces the receipts that already declared its charges: the receipts issuing it would void, by number (or id while one is still waiting for its number), in issue order. Absent when nothing would be replaced. | [optional] 
**receipt_replacement_conflict** | **str** | Why an invoice over this selection could not replace the receipts behind it — a receipt still being signed, or a covered charge not taken in full. The same message the create request refuses with, so a client can block issuing before submit. Absent when it can. | [optional] 

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


