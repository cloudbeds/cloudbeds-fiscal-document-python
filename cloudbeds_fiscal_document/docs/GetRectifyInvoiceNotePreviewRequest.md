# GetRectifyInvoiceNotePreviewRequest

Request to create a rectifying invoice. Only available for Spanish properties.  **Important:** The specified invoice must not have been previously rectified. If it has been rectified, you must rectify the most recent invoice in the rectification chain instead. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** | ID of the invoice to be rectified.  **Validation:** This invoice must not have been previously rectified according to Spanish fiscal regulations.  | 
**reason** | **str** | Reason for rectifying the invoice | [optional] 
**user_id** | **int** | ID of the user creating the rectification | [optional] 
**method** | [**CreationMethod**](CreationMethod.md) |  | 
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs associated with selected folio IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.get_rectify_invoice_note_preview_request import GetRectifyInvoiceNotePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRectifyInvoiceNotePreviewRequest from a JSON string
get_rectify_invoice_note_preview_request_instance = GetRectifyInvoiceNotePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(GetRectifyInvoiceNotePreviewRequest.to_json())

# convert the object into a dict
get_rectify_invoice_note_preview_request_dict = get_rectify_invoice_note_preview_request_instance.to_dict()
# create an instance of GetRectifyInvoiceNotePreviewRequest from a dict
get_rectify_invoice_note_preview_request_from_dict = GetRectifyInvoiceNotePreviewRequest.from_dict(get_rectify_invoice_note_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


