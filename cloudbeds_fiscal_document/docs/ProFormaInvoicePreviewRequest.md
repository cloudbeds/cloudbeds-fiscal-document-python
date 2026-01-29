# ProFormaInvoicePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | List of pending transaction IDs to include in the pro forma invoice (deprecated, use &#x60;includeTransactionIds&#x60; instead) | 
**transaction_id_to_amount** | **Dict[str, int]** | Map of transaction ID to amount for partial transaction inclusion | [optional] 
**payment_ids** | **List[int]** | List of payment IDs associated with the pending transactions | [optional] 
**source_id** | **int** |  | 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**user_id** | **int** |  | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | 
**invoice_date** | **date** | Date for the pro forma invoice (defaults to current date if not provided) | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.pro_forma_invoice_preview_request import ProFormaInvoicePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProFormaInvoicePreviewRequest from a JSON string
pro_forma_invoice_preview_request_instance = ProFormaInvoicePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(ProFormaInvoicePreviewRequest.to_json())

# convert the object into a dict
pro_forma_invoice_preview_request_dict = pro_forma_invoice_preview_request_instance.to_dict()
# create an instance of ProFormaInvoicePreviewRequest from a dict
pro_forma_invoice_preview_request_from_dict = ProFormaInvoicePreviewRequest.from_dict(pro_forma_invoice_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


