# GetInvoicePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | 
**source_id** | **int** |  | 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**user_id** | **int** |  | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 
**simplified** | **bool** |  | [optional] [default to False]

## Example

```python
from cloudbeds_fiscal_document.models.get_invoice_preview_request import GetInvoicePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoicePreviewRequest from a JSON string
get_invoice_preview_request_instance = GetInvoicePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(GetInvoicePreviewRequest.to_json())

# convert the object into a dict
get_invoice_preview_request_dict = get_invoice_preview_request_instance.to_dict()
# create an instance of GetInvoicePreviewRequest from a dict
get_invoice_preview_request_from_dict = GetInvoicePreviewRequest.from_dict(get_invoice_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


