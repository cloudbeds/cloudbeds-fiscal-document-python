# FiscalDocumentDetailedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_full_name** | **str** |  | [optional] 
**source_name** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**invoice_date_property_timezone** | **date** |  | [optional] 
**file_name** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**due_date** | **date** |  | [optional] 
**due_date_property_timezone** | **date** |  | [optional] 
**recipients** | [**List[RecipientDetails]**](RecipientDetails.md) |  | [optional] 
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**origin** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fail_reason** | **str** |  | [optional] 
**method** | [**CreationMethod**](CreationMethod.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**government_integration** | [**GovernmentIntegration**](GovernmentIntegration.md) |  | [optional] 
**latest_linked_document** | [**LatestLinkedDocument**](LatestLinkedDocument.md) |  | [optional] 
**linked_documents** | [**List[LinkedDocument]**](LinkedDocument.md) | List of documents linked to this fiscal document (both parent and child relationships) | [optional] 
**actions** | [**List[Action]**](Action.md) | Returns the list of actions available for the transaction | [optional] 
**source_identifier** | **str** | Reservation Identifier or a group code | [optional] 
**simplified** | **bool** | Applies to invoices only. | [optional] 

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


