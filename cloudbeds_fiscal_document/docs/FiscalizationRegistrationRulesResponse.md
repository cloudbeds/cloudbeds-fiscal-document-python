# FiscalizationRegistrationRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryInfo**](CountryInfo.md) |  | 
**fields** | [**List[FieldDefinition]**](FieldDefinition.md) |  | 
**sections** | [**List[RulesSection]**](RulesSection.md) | Ordered list of UI sections that host the country&#39;s fields. The frontend uses this list to render sub-navigation; each field references a section via its sectionKey. When absent, all fields belong to an implicit \&quot;registration\&quot; section. | [optional] 
**examples** | **Dict[str, str]** | Example values for common fields | [optional] 
**requires** | [**CountryRequirements**](CountryRequirements.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_registration_rules_response import FiscalizationRegistrationRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationRegistrationRulesResponse from a JSON string
fiscalization_registration_rules_response_instance = FiscalizationRegistrationRulesResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationRegistrationRulesResponse.to_json())

# convert the object into a dict
fiscalization_registration_rules_response_dict = fiscalization_registration_rules_response_instance.to_dict()
# create an instance of FiscalizationRegistrationRulesResponse from a dict
fiscalization_registration_rules_response_from_dict = FiscalizationRegistrationRulesResponse.from_dict(fiscalization_registration_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


