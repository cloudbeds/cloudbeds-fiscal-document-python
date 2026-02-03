# CreateInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | 
**transaction_id_to_amount** | **Dict[str, float]** | Map of transaction ID to amount (in major currency units, e.g., 10.50 for $10.50) for partial transaction inclusion | [optional] 
**source_id** | **int** |  | 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**user_id** | **int** |  | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | [optional] 
**manual_recipient** | [**ManualRecipientRequest**](ManualRecipientRequest.md) |  | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 
**simplified** | **bool** |  | [optional] [default to False]
**due_date_property_timezone** | **date** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.create_invoice_request import CreateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequest from a JSON string
create_invoice_request_instance = CreateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequest.to_json())

# convert the object into a dict
create_invoice_request_dict = create_invoice_request_instance.to_dict()
# create an instance of CreateInvoiceRequest from a dict
create_invoice_request_from_dict = CreateInvoiceRequest.from_dict(create_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


