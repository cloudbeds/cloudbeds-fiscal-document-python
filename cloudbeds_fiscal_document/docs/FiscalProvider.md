# FiscalProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**channel** | [**FiscalProviderChannel**](FiscalProviderChannel.md) |  | 
**onboarding** | [**List[FiscalProviderOnboardingStep]**](FiscalProviderOnboardingStep.md) | Ordered wizard steps (key references into sections). Must complete before activation. | 
**sections** | [**List[FiscalProviderSection]**](FiscalProviderSection.md) | All tabs — includes onboarding steps (editable) plus post-setup config. | 
**flows** | **List[str]** | Flow IDs this provider handles. Routing is only auto-seeded for these. | 
**visual** | [**FiscalProviderVisual**](FiscalProviderVisual.md) |  | [optional] 
**enabled** | **bool** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_provider import FiscalProvider

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalProvider from a JSON string
fiscal_provider_instance = FiscalProvider.from_json(json)
# print the JSON string representation of the object
print(FiscalProvider.to_json())

# convert the object into a dict
fiscal_provider_dict = fiscal_provider_instance.to_dict()
# create an instance of FiscalProvider from a dict
fiscal_provider_from_dict = FiscalProvider.from_dict(fiscal_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


