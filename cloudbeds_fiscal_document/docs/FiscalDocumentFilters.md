# FiscalDocumentFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of IDs to filter by | [optional] 
**source_ids** | **List[str]** | List of source IDs to filter by | [optional] 
**source_identifiers** | **List[str]** | List of source-specific identifiers | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**source_kinds** | [**List[SourceKind]**](SourceKind.md) | Filter by source kind | [optional] 
**number_contains** | **str** | Filter by document number partial match | [optional] 
**statuses** | [**List[FiscalDocumentStatus]**](FiscalDocumentStatus.md) | List of fiscal document statuses to filter by | [optional] 
**kinds** | [**List[FiscalDocumentKind]**](FiscalDocumentKind.md) | List of fiscal document kinds to filter by | [optional] 
**created_at_from** | **datetime** | Creation date-time range start | [optional] 
**created_at_to** | **datetime** | Creation date-time range end | [optional] 
**invoice_date_from** | **date** | Invoice date range start | [optional] 
**invoice_date_to** | **date** | Invoice date range end | [optional] 
**invoice_date_property_timezone_from** | **date** | Invoice date range start | [optional] 
**invoice_date_property_timezone_to** | **date** | Invoice date range end | [optional] 
**due_date_from** | **date** | Due date range start | [optional] 
**due_date_to** | **date** | Due date range end | [optional] 
**due_date_property_timezone_from** | **date** | Due date range start | [optional] 
**due_date_property_timezone_to** | **date** | Due date range end | [optional] 
**amount_from** | **float** | Minimum document amount | [optional] 
**amount_to** | **float** | Maximum document amount | [optional] 
**balance_from** | **float** | Minimum document balance | [optional] 
**balance_to** | **float** | Maximum document balance | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_filters import FiscalDocumentFilters

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentFilters from a JSON string
fiscal_document_filters_instance = FiscalDocumentFilters.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentFilters.to_json())

# convert the object into a dict
fiscal_document_filters_dict = fiscal_document_filters_instance.to_dict()
# create an instance of FiscalDocumentFilters from a dict
fiscal_document_filters_from_dict = FiscalDocumentFilters.from_dict(fiscal_document_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


