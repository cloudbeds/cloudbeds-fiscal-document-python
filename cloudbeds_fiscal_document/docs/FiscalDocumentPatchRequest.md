# FiscalDocumentPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**fail_reason** | **str** |  | [optional] 
**government_integration** | [**GovernmentIntegration**](GovernmentIntegration.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_patch_request import FiscalDocumentPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentPatchRequest from a JSON string
fiscal_document_patch_request_instance = FiscalDocumentPatchRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentPatchRequest.to_json())

# convert the object into a dict
fiscal_document_patch_request_dict = fiscal_document_patch_request_instance.to_dict()
# create an instance of FiscalDocumentPatchRequest from a dict
fiscal_document_patch_request_from_dict = FiscalDocumentPatchRequest.from_dict(fiscal_document_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


