# GetFolioExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folio_ids** | **List[int]** | Include transactions from the specified folio IDs | 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**source_id** | **int** | source ID of folio | 
**credit_debit_view** | **bool** | Should transactions be separated into debit/credits | [optional] 
**revenue_compact** | **bool** | Compact revenue transactions, valid only for sourceKind &#x3D; RESERVATION | [optional] 
**date_from** | **date** | Minimum date, only for sourceKind &#x3D; HOUSE_ACCOUNT | [optional] 
**date_to** | **date** | Maximum date, only for sourceKind &#x3D; HOUSE_ACCOUNT, optional | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.get_folio_export_request import GetFolioExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFolioExportRequest from a JSON string
get_folio_export_request_instance = GetFolioExportRequest.from_json(json)
# print the JSON string representation of the object
print(GetFolioExportRequest.to_json())

# convert the object into a dict
get_folio_export_request_dict = get_folio_export_request_instance.to_dict()
# create an instance of GetFolioExportRequest from a dict
get_folio_export_request_from_dict = GetFolioExportRequest.from_dict(get_folio_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


