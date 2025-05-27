# FiscalDocumentTransactionsPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[FiscalDocumentTransactionResponse]**](FiscalDocumentTransactionResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_transactions_paginated import FiscalDocumentTransactionsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentTransactionsPaginated from a JSON string
fiscal_document_transactions_paginated_instance = FiscalDocumentTransactionsPaginated.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentTransactionsPaginated.to_json())

# convert the object into a dict
fiscal_document_transactions_paginated_dict = fiscal_document_transactions_paginated_instance.to_dict()
# create an instance of FiscalDocumentTransactionsPaginated from a dict
fiscal_document_transactions_paginated_from_dict = FiscalDocumentTransactionsPaginated.from_dict(fiscal_document_transactions_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


