# CreateReceiptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**List[ReceiptTransactionAllocation]**](ReceiptTransactionAllocation.md) |  | [optional] 
**transaction_id** | **int** | Id of the transaction associated to a payment. This parameter is mutually exclusive with &#x60;paymentId&#x60;.  | [optional] 
**payment_id** | **int** | Id of the payment. This parameter is mutually exclusive with &#x60;transactionId&#x60;.  | [optional] 
**sequence_id** | **int** |  | [optional] 
**user_id** | **int** |  | 
**source_id** | **int** |  | 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.create_receipt_request import CreateReceiptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReceiptRequest from a JSON string
create_receipt_request_instance = CreateReceiptRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReceiptRequest.to_json())

# convert the object into a dict
create_receipt_request_dict = create_receipt_request_instance.to_dict()
# create an instance of CreateReceiptRequest from a dict
create_receipt_request_from_dict = CreateReceiptRequest.from_dict(create_receipt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


