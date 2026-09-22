# FiscalProviderOnboardingStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | References a section key. | 
**required** | **bool** | Blocks onboarding completion when incomplete. | [optional] [default to False]

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_provider_onboarding_step import FiscalProviderOnboardingStep

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalProviderOnboardingStep from a JSON string
fiscal_provider_onboarding_step_instance = FiscalProviderOnboardingStep.from_json(json)
# print the JSON string representation of the object
print(FiscalProviderOnboardingStep.to_json())

# convert the object into a dict
fiscal_provider_onboarding_step_dict = fiscal_provider_onboarding_step_instance.to_dict()
# create an instance of FiscalProviderOnboardingStep from a dict
fiscal_provider_onboarding_step_from_dict = FiscalProviderOnboardingStep.from_dict(fiscal_provider_onboarding_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


