# FiscalDocumentEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_email_request import FiscalDocumentEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentEmailRequest from a JSON string
fiscal_document_email_request_instance = FiscalDocumentEmailRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentEmailRequest.to_json())

# convert the object into a dict
fiscal_document_email_request_dict = fiscal_document_email_request_instance.to_dict()
# create an instance of FiscalDocumentEmailRequest from a dict
fiscal_document_email_request_from_dict = FiscalDocumentEmailRequest.from_dict(fiscal_document_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


