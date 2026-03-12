# FiscalizationConsentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consented** | **bool** | Whether the property has provided consent | 
**consented_at** | **datetime** | When consent was provided | [optional] 
**consented_by** | **str** | Who provided consent | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_consent_response import FiscalizationConsentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationConsentResponse from a JSON string
fiscalization_consent_response_instance = FiscalizationConsentResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationConsentResponse.to_json())

# convert the object into a dict
fiscalization_consent_response_dict = fiscalization_consent_response_instance.to_dict()
# create an instance of FiscalizationConsentResponse from a dict
fiscalization_consent_response_from_dict = FiscalizationConsentResponse.from_dict(fiscalization_consent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


