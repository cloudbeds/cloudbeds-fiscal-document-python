# FiscalDocumentSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**government_integration** | [**GovernmentIntegration**](GovernmentIntegration.md) |  | [optional] 
**linked_to** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentSummaryResponse from a JSON string
fiscal_document_summary_response_instance = FiscalDocumentSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentSummaryResponse.to_json())

# convert the object into a dict
fiscal_document_summary_response_dict = fiscal_document_summary_response_instance.to_dict()
# create an instance of FiscalDocumentSummaryResponse from a dict
fiscal_document_summary_response_from_dict = FiscalDocumentSummaryResponse.from_dict(fiscal_document_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


