# FiscalDocumentDetailedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_full_name** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_kind** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**file_name** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**due_date** | **date** |  | [optional] 
**guests** | [**List[GuestDetails]**](GuestDetails.md) |  | [optional] 
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**external_source** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**government_integration** | [**GovernmentIntegration**](GovernmentIntegration.md) |  | [optional] 
**actions** | [**List[Action]**](Action.md) | Returns the list of actions available for the transaction | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_detailed_response import FiscalDocumentDetailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentDetailedResponse from a JSON string
fiscal_document_detailed_response_instance = FiscalDocumentDetailedResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentDetailedResponse.to_json())

# convert the object into a dict
fiscal_document_detailed_response_dict = fiscal_document_detailed_response_instance.to_dict()
# create an instance of FiscalDocumentDetailedResponse from a dict
fiscal_document_detailed_response_from_dict = FiscalDocumentDetailedResponse.from_dict(fiscal_document_detailed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


