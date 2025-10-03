# FiscalDocumentTransactionAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipt_number** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_transaction_allocation import FiscalDocumentTransactionAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentTransactionAllocation from a JSON string
fiscal_document_transaction_allocation_instance = FiscalDocumentTransactionAllocation.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentTransactionAllocation.to_json())

# convert the object into a dict
fiscal_document_transaction_allocation_dict = fiscal_document_transaction_allocation_instance.to_dict()
# create an instance of FiscalDocumentTransactionAllocation from a dict
fiscal_document_transaction_allocation_from_dict = FiscalDocumentTransactionAllocation.from_dict(fiscal_document_transaction_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


