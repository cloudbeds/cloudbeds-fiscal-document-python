# InvoiceTransactionAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** | Invoice transaction ID that received the allocation | [optional] 
**allocated_amount** | **float** | Total amount allocated to this transaction from all receipts | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.invoice_transaction_allocation import InvoiceTransactionAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTransactionAllocation from a JSON string
invoice_transaction_allocation_instance = InvoiceTransactionAllocation.from_json(json)
# print the JSON string representation of the object
print(InvoiceTransactionAllocation.to_json())

# convert the object into a dict
invoice_transaction_allocation_dict = invoice_transaction_allocation_instance.to_dict()
# create an instance of InvoiceTransactionAllocation from a dict
invoice_transaction_allocation_from_dict = InvoiceTransactionAllocation.from_dict(invoice_transaction_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


