# TransactionsSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**source_id** | **int** | Source ID. | 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**folio_ids** | **List[int]** | Filter by folio IDs. | [optional] 
**exclude_transaction_ids** | **List[int]** | Transaction IDs to exclude. | [optional] 
**include_transaction_ids** | **List[int]** | Transaction IDs to include. | [optional] 
**transaction_id_to_amount** | **Dict[str, float]** | Map of transaction ID to amount (in major currency units, e.g., 10.50 for $10.50) for partial transaction inclusion. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.transactions_summary_request import TransactionsSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsSummaryRequest from a JSON string
transactions_summary_request_instance = TransactionsSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionsSummaryRequest.to_json())

# convert the object into a dict
transactions_summary_request_dict = transactions_summary_request_instance.to_dict()
# create an instance of TransactionsSummaryRequest from a dict
transactions_summary_request_from_dict = TransactionsSummaryRequest.from_dict(transactions_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


