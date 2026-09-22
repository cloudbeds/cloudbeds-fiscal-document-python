# FiscalConnectionOnboarding

Onboarding progress. Present when the connection has required setup steps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**current** | [**FiscalConnectionOnboardingCurrent**](FiscalConnectionOnboardingCurrent.md) |  | [optional] 
**progress** | **str** | e.g. Paused at \&quot;Certificate\&quot; · Step 2 of 3 | [optional] 
**done** | **bool** |  | [optional] 
**failed** | [**FiscalConnectionOnboardingFailed**](FiscalConnectionOnboardingFailed.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_onboarding import FiscalConnectionOnboarding

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionOnboarding from a JSON string
fiscal_connection_onboarding_instance = FiscalConnectionOnboarding.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionOnboarding.to_json())

# convert the object into a dict
fiscal_connection_onboarding_dict = fiscal_connection_onboarding_instance.to_dict()
# create an instance of FiscalConnectionOnboarding from a dict
fiscal_connection_onboarding_from_dict = FiscalConnectionOnboarding.from_dict(fiscal_connection_onboarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


