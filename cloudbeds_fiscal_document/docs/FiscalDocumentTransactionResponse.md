# FiscalDocumentTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_identifier** | **str** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**transaction_date** | **datetime** |  | [optional] 
**guest_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**internal_code** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**available_amount** | **float** |  | [optional] 
**document_fiscalized_amount** | **float** | Will be null if filter is not by document id | [optional] 
**currency** | **str** | Original transaction currency code. | [optional] 
**display_currency** | **str** | Currency code used for the display amounts in this response. | [optional] 
**display_amount** | **float** | Amount converted to the display currency. | [optional] 
**display_available_amount** | **float** | Available amount converted to the display currency. | [optional] 
**display_document_fiscalized_amount** | **float** | Document fiscalized amount converted to the display currency. | [optional] 
**folio_id** | **str** |  | [optional] 
**status** | **str** | Status of the transaction - PENDING for unpaid transactions, POSTED for paid transactions | [optional] 
**paid_amount** | **float** |  | [optional] 
**allocations** | [**List[FiscalDocumentTransactionAllocation]**](FiscalDocumentTransactionAllocation.md) |  | [optional] 
**taxes** | [**List[FiscalDocumentTransactionResponse]**](FiscalDocumentTransactionResponse.md) | Child VAT taxes of this transaction. Populated only when nestTaxes&#x3D;true; taxes not classified as VAT are never nested here and are returned as top-level transactions instead. | [optional] 
**invoiced_status** | [**InvoicedStatus**](InvoicedStatus.md) |  | [optional] 

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


