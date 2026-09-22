# SeriesDocumentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_kind** | **str** | Unique series slot identifier (e.g. INVOICE, INVOICE:NFSE) | 
**prefix** | **str** | Series prefix hint (e.g. FT for Portugal, NFSE for Brazil) | 
**name** | **str** | Display name (e.g., \&quot;Fatura (Standard Invoice)\&quot;) | 

## Example

```python
from cloudbeds_fiscal_document.models.series_document_type import SeriesDocumentType

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesDocumentType from a JSON string
series_document_type_instance = SeriesDocumentType.from_json(json)
# print the JSON string representation of the object
print(SeriesDocumentType.to_json())

# convert the object into a dict
series_document_type_dict = series_document_type_instance.to_dict()
# create an instance of SeriesDocumentType from a dict
series_document_type_from_dict = SeriesDocumentType.from_dict(series_document_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


