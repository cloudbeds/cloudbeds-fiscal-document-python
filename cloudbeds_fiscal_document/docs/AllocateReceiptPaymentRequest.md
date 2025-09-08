# AllocateReceiptPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**List[ReceiptTransactionAllocation]**](ReceiptTransactionAllocation.md) |  | 
**receipt_id** | **int** | Id of the receipt.  | 

## Example

```python
from cloudbeds_fiscal_document.models.allocate_receipt_payment_request import AllocateReceiptPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllocateReceiptPaymentRequest from a JSON string
allocate_receipt_payment_request_instance = AllocateReceiptPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(AllocateReceiptPaymentRequest.to_json())

# convert the object into a dict
allocate_receipt_payment_request_dict = allocate_receipt_payment_request_instance.to_dict()
# create an instance of AllocateReceiptPaymentRequest from a dict
allocate_receipt_payment_request_from_dict = AllocateReceiptPaymentRequest.from_dict(allocate_receipt_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


