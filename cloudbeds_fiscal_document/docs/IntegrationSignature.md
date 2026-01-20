# IntegrationSignature

A semantic signature/response item from a government integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Semantic type (JWT_TOKEN, QR_CODE_DATA, TRANSACTION_ID, COMPLIANCE_CHECK, etc.) | [optional] 
**label** | **str** | Human-readable display label. | [optional] 
**value** | **str** | The actual signature data/value. | [optional] 
**format** | **str** | Format of the value. | [optional] 
**source** | **str** | Source integration (FISKALTRUST_FR, FISKALTRUST_IT, etc.) | [optional] 
**raw_metadata** | **Dict[str, str]** | Original integration-specific codes for debugging/auditing. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.integration_signature import IntegrationSignature

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSignature from a JSON string
integration_signature_instance = IntegrationSignature.from_json(json)
# print the JSON string representation of the object
print(IntegrationSignature.to_json())

# convert the object into a dict
integration_signature_dict = integration_signature_instance.to_dict()
# create an instance of IntegrationSignature from a dict
integration_signature_from_dict = IntegrationSignature.from_dict(integration_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


