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
**files** | [**List[FiscalDocumentFile]**](FiscalDocumentFile.md) | All files available for this document, primary first followed by any additional stored files (e.g. the Portuguese duplicate). Always present as an array, but may be empty for documents whose file has not been generated yet (e.g. REQUESTED or early FAILED status). The primary file entry, when present, has a null id (the download endpoint serves it without a fileId; additional entries are downloaded by passing their id as the fileId query parameter).  | 
**amount** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**due_date** | **date** |  | [optional] 
**due_date_property_timezone** | **date** |  | [optional] 
**recipients** | [**List[RecipientDetails]**](RecipientDetails.md) |  | [optional] 
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**origin** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fail_reason** | **str** |  | [optional] 
**reason** | **str** | Correction reason recorded when the document was created (credit notes and rectifying invoices). One of the slugs offered by the credit-note action&#39;s reason field, or free text on the Spanish rectify path. Null when no reason was given. | [optional] 
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
**require_attention** | **bool** | Indicates whether this document requires manual attention. | [optional] 
**has_discrepancies** | **bool** | Indicates whether this document has pending transaction discrepancies. | [optional] 
**package_breakdown** | **bool** | Per-document override for package breakdown. Null means use property default. | [optional] 
**currency** | **str** | Currency the document amount is expressed in. Equals the invoice/document currency, which may differ from the property base currency when a foreign-currency invoice was issued. | [optional] 
**property_currency** | **str** | The property&#39;s base currency code. | [optional] 
**property_currency_amount** | **float** | The document amount converted to the property&#39;s base currency using the property&#39;s configured exchange rates. Null when the document currency already equals the property base currency (no conversion needed). | [optional] 

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


