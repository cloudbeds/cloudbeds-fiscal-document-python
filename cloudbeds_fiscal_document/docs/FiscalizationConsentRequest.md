# FiscalizationConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consented_by** | **str** | Identifier of the user who provided consent (e.g., email or user ID) | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_consent_request import FiscalizationConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationConsentRequest from a JSON string
fiscalization_consent_request_instance = FiscalizationConsentRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalizationConsentRequest.to_json())

# convert the object into a dict
fiscalization_consent_request_dict = fiscalization_consent_request_instance.to_dict()
# create an instance of FiscalizationConsentRequest from a dict
fiscalization_consent_request_from_dict = FiscalizationConsentRequest.from_dict(fiscalization_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


