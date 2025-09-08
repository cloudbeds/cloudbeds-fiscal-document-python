# FiscalDocumentTransactionsForAllocationPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionForAllocationResponse]**](TransactionForAllocationResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_transactions_for_allocation_paginated import FiscalDocumentTransactionsForAllocationPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentTransactionsForAllocationPaginated from a JSON string
fiscal_document_transactions_for_allocation_paginated_instance = FiscalDocumentTransactionsForAllocationPaginated.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentTransactionsForAllocationPaginated.to_json())

# convert the object into a dict
fiscal_document_transactions_for_allocation_paginated_dict = fiscal_document_transactions_for_allocation_paginated_instance.to_dict()
# create an instance of FiscalDocumentTransactionsForAllocationPaginated from a dict
fiscal_document_transactions_for_allocation_paginated_from_dict = FiscalDocumentTransactionsForAllocationPaginated.from_dict(fiscal_document_transactions_for_allocation_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


