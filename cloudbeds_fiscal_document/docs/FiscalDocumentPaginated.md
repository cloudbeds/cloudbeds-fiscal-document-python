# FiscalDocumentPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_documents** | [**List[FiscalDocumentDetailedResponse]**](FiscalDocumentDetailedResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_paginated import FiscalDocumentPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentPaginated from a JSON string
fiscal_document_paginated_instance = FiscalDocumentPaginated.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentPaginated.to_json())

# convert the object into a dict
fiscal_document_paginated_dict = fiscal_document_paginated_instance.to_dict()
# create an instance of FiscalDocumentPaginated from a dict
fiscal_document_paginated_from_dict = FiscalDocumentPaginated.from_dict(fiscal_document_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


