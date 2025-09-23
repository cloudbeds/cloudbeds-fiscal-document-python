# RectifyInvoiceNoteRequest

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
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.rectify_invoice_note_request import RectifyInvoiceNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RectifyInvoiceNoteRequest from a JSON string
rectify_invoice_note_request_instance = RectifyInvoiceNoteRequest.from_json(json)
# print the JSON string representation of the object
print(RectifyInvoiceNoteRequest.to_json())

# convert the object into a dict
rectify_invoice_note_request_dict = rectify_invoice_note_request_instance.to_dict()
# create an instance of RectifyInvoiceNoteRequest from a dict
rectify_invoice_note_request_from_dict = RectifyInvoiceNoteRequest.from_dict(rectify_invoice_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


