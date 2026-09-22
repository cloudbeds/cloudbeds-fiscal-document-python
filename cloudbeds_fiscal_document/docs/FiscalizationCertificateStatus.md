# FiscalizationCertificateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** | Whether the certificate has been verified by the provider | [optional] 
**created_at** | **datetime** | When the certificate was first uploaded | 
**updated_at** | **datetime** | When the certificate was last updated | 
**expires_at** | **datetime** | Certificate notAfter date parsed from the uploaded X.509 certificate. Null when not applicable or not yet parsed. | [optional] 
**provider_valid** | **bool** | Live provider validity — true when the provider reports the certificate as valid and accepted. Null when the provider check was skipped or unavailable. | [optional] 
**invalid_reason** | **str** | Provider-reported reason for invalidity (e.g. HR_1002). Only present when providerValid is false. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_certificate_status import FiscalizationCertificateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationCertificateStatus from a JSON string
fiscalization_certificate_status_instance = FiscalizationCertificateStatus.from_json(json)
# print the JSON string representation of the object
print(FiscalizationCertificateStatus.to_json())

# convert the object into a dict
fiscalization_certificate_status_dict = fiscalization_certificate_status_instance.to_dict()
# create an instance of FiscalizationCertificateStatus from a dict
fiscalization_certificate_status_from_dict = FiscalizationCertificateStatus.from_dict(fiscalization_certificate_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


