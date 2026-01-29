# InvoiceAllocationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**List[InvoiceTransactionAllocation]**](InvoiceTransactionAllocation.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.invoice_allocations_response import InvoiceAllocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAllocationsResponse from a JSON string
invoice_allocations_response_instance = InvoiceAllocationsResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceAllocationsResponse.to_json())

# convert the object into a dict
invoice_allocations_response_dict = invoice_allocations_response_instance.to_dict()
# create an instance of InvoiceAllocationsResponse from a dict
invoice_allocations_response_from_dict = InvoiceAllocationsResponse.from_dict(invoice_allocations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


