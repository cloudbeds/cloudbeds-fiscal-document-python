# CreateSettlementInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 
**transaction_id_to_amount** | **Dict[str, float]** | Map of transaction ID to amount (in major currency units, e.g., 10.50 for $10.50) for partial transaction inclusion | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | [optional] 
**manual_recipient** | [**ManualRecipientRequest**](ManualRecipientRequest.md) |  | [optional] 
**sequence_id** | **int** |  | [optional] 
**due_date_property_timezone** | **date** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.create_settlement_invoice_request import CreateSettlementInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSettlementInvoiceRequest from a JSON string
create_settlement_invoice_request_instance = CreateSettlementInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSettlementInvoiceRequest.to_json())

# convert the object into a dict
create_settlement_invoice_request_dict = create_settlement_invoice_request_instance.to_dict()
# create an instance of CreateSettlementInvoiceRequest from a dict
create_settlement_invoice_request_from_dict = CreateSettlementInvoiceRequest.from_dict(create_settlement_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


