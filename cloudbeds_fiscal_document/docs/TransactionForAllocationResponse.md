# TransactionForAllocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**transaction_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**internal_code** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**allocated_amount** | **float** |  | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**taxes** | [**List[TransactionForAllocationResponse]**](TransactionForAllocationResponse.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.transaction_for_allocation_response import TransactionForAllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionForAllocationResponse from a JSON string
transaction_for_allocation_response_instance = TransactionForAllocationResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionForAllocationResponse.to_json())

# convert the object into a dict
transaction_for_allocation_response_dict = transaction_for_allocation_response_instance.to_dict()
# create an instance of TransactionForAllocationResponse from a dict
transaction_for_allocation_response_from_dict = TransactionForAllocationResponse.from_dict(transaction_for_allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


