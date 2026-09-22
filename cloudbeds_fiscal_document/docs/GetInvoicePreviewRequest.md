# GetInvoicePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id_to_amount** | **Dict[str, float]** | Map of transaction ID to amount (in major currency units, e.g., 10.50 for $10.50) for partial transaction inclusion | [optional] 
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | 
**source_id** | **int** |  | 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**user_id** | **int** |  | [optional] 
**currency** | **str** | Invoice currency. Selected transactions are converted into this currency at creation using the property&#39;s current exchange rate, which is locked on the issued document, and the converted amounts are fiscalized. Defaults to the property currency when omitted. | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | [optional] 
**manual_recipient** | [**ManualRecipientRequest**](ManualRecipientRequest.md) |  | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 
**simplified** | **bool** |  | [optional] [default to False]
**package_breakdown** | **bool** | Per-document override for package breakdown. Null means use property default. | [optional] 
**due_date_property_timezone** | **date** |  | [optional] 

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


