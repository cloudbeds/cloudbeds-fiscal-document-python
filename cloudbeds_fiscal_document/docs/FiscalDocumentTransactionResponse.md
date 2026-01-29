# FiscalDocumentTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**transaction_date** | **datetime** |  | [optional] 
**guest_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**internal_code** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**available_amount** | **float** |  | [optional] 
**folio_id** | **str** |  | [optional] 
**status** | **str** | Status of the transaction - PENDING for unpaid transactions, POSTED for paid transactions | [optional] 
**paid_amount** | **float** |  | [optional] 
**allocations** | [**List[FiscalDocumentTransactionAllocation]**](FiscalDocumentTransactionAllocation.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_transaction_response import FiscalDocumentTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentTransactionResponse from a JSON string
fiscal_document_transaction_response_instance = FiscalDocumentTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentTransactionResponse.to_json())

# convert the object into a dict
fiscal_document_transaction_response_dict = fiscal_document_transaction_response_instance.to_dict()
# create an instance of FiscalDocumentTransactionResponse from a dict
fiscal_document_transaction_response_from_dict = FiscalDocumentTransactionResponse.from_dict(fiscal_document_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


