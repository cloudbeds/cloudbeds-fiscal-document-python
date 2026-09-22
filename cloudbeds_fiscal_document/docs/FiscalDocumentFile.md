# FiscalDocumentFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the stored file, passed as the download endpoint&#39;s fileId query parameter. Null for the primary file (the document itself), which the download endpoint serves without a fileId. | [optional] 
**category** | [**FiscalDocumentFileCategory**](FiscalDocumentFileCategory.md) |  | 
**mime_type** | **str** | Mime type of the file, derived from its extension (e.g. application/pdf). | 
**filename** | **str** | Display file name, including extension. | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_file import FiscalDocumentFile

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentFile from a JSON string
fiscal_document_file_instance = FiscalDocumentFile.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentFile.to_json())

# convert the object into a dict
fiscal_document_file_dict = fiscal_document_file_instance.to_dict()
# create an instance of FiscalDocumentFile from a dict
fiscal_document_file_from_dict = FiscalDocumentFile.from_dict(fiscal_document_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


