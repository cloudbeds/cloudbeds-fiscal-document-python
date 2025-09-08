# CreateSimpleReceiptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | Ids of the transactions associated to payments | 
**sequence_id** | **int** |  | [optional] 
**user_id** | **int** |  | 
**source_id** | **int** |  | 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.create_simple_receipt_request import CreateSimpleReceiptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSimpleReceiptRequest from a JSON string
create_simple_receipt_request_instance = CreateSimpleReceiptRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSimpleReceiptRequest.to_json())

# convert the object into a dict
create_simple_receipt_request_dict = create_simple_receipt_request_instance.to_dict()
# create an instance of CreateSimpleReceiptRequest from a dict
create_simple_receipt_request_from_dict = CreateSimpleReceiptRequest.from_dict(create_simple_receipt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


