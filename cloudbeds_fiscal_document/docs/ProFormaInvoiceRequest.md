# ProFormaInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | List of pending transaction IDs to include in the pro forma invoice (deprecated, use &#x60;includeTransactionIds&#x60; instead) | 
**payment_ids** | **List[int]** | List of payment IDs associated with the pending transactions | [optional] 
**source_id** | **int** |  | 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**user_id** | **int** |  | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | 
**invoice_date** | **date** | Date for the pro forma invoice (defaults to current date if not provided) | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs associated with selected folio IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.pro_forma_invoice_request import ProFormaInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProFormaInvoiceRequest from a JSON string
pro_forma_invoice_request_instance = ProFormaInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(ProFormaInvoiceRequest.to_json())

# convert the object into a dict
pro_forma_invoice_request_dict = pro_forma_invoice_request_instance.to_dict()
# create an instance of ProFormaInvoiceRequest from a dict
pro_forma_invoice_request_from_dict = ProFormaInvoiceRequest.from_dict(pro_forma_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


