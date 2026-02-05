# ReceiptTransactionAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** |  | 
**amount** | **float** |  | 
**document_id** | **int** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.receipt_transaction_allocation import ReceiptTransactionAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptTransactionAllocation from a JSON string
receipt_transaction_allocation_instance = ReceiptTransactionAllocation.from_json(json)
# print the JSON string representation of the object
print(ReceiptTransactionAllocation.to_json())

# convert the object into a dict
receipt_transaction_allocation_dict = receipt_transaction_allocation_instance.to_dict()
# create an instance of ReceiptTransactionAllocation from a dict
receipt_transaction_allocation_from_dict = ReceiptTransactionAllocation.from_dict(receipt_transaction_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


