# FiscalConnectionOnboardingFailed

Present when the connection is in ERROR and a specific step caused the failure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_onboarding_failed import FiscalConnectionOnboardingFailed

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionOnboardingFailed from a JSON string
fiscal_connection_onboarding_failed_instance = FiscalConnectionOnboardingFailed.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionOnboardingFailed.to_json())

# convert the object into a dict
fiscal_connection_onboarding_failed_dict = fiscal_connection_onboarding_failed_instance.to_dict()
# create an instance of FiscalConnectionOnboardingFailed from a dict
fiscal_connection_onboarding_failed_from_dict = FiscalConnectionOnboardingFailed.from_dict(fiscal_connection_onboarding_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


