# FolioExportSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Sort field name. One of: transaction_datetime, service_date, internal_code, description, notes, quantity, amount.  | 
**direction** | **str** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.folio_export_sort import FolioExportSort

# TODO update the JSON string below
json = "{}"
# create an instance of FolioExportSort from a JSON string
folio_export_sort_instance = FolioExportSort.from_json(json)
# print the JSON string representation of the object
print(FolioExportSort.to_json())

# convert the object into a dict
folio_export_sort_dict = folio_export_sort_instance.to_dict()
# create an instance of FolioExportSort from a dict
folio_export_sort_from_dict = FolioExportSort.from_dict(folio_export_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


