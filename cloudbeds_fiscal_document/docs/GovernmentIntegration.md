# GovernmentIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | [optional] 
**series** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**qr** | [**GovernmentIntegrationQr**](GovernmentIntegrationQr.md) |  | [optional] 
**url** | **str** |  | [optional] 
**official_id** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**rectifying_invoice_type** | **str** |  | [optional] 
**cancellation_failed_fallback_status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**pdf_file_base64** | **bytearray** | Base64-encoded PDF file content. Only allowed when status is COMPLETED_INTEGRATION. | [optional] 
**handwritten** | **bool** | Indicates this is a handwritten receipt created during POS unavailability. | [optional] 
**signatures** | [**List[IntegrationSignature]**](IntegrationSignature.md) | Array of semantic signatures/response data from the government integration. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.government_integration import GovernmentIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of GovernmentIntegration from a JSON string
government_integration_instance = GovernmentIntegration.from_json(json)
# print the JSON string representation of the object
print(GovernmentIntegration.to_json())

# convert the object into a dict
government_integration_dict = government_integration_instance.to_dict()
# create an instance of GovernmentIntegration from a dict
government_integration_from_dict = GovernmentIntegration.from_dict(government_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


