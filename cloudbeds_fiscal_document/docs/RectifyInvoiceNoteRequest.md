# RectifyInvoiceNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** |  | 
**reason** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**method** | [**CreationMethod**](CreationMethod.md) |  | 
**transaction_ids** | **List[int]** |  | [optional] 

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


