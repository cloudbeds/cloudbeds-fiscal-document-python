# RulesSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable identifier for the section (e.g., \&quot;registration\&quot;, \&quot;customization.branding\&quot;, \&quot;customization.invoicing\&quot;). | 
**label** | **str** | Display label for the section (translated) | 
**description** | **str** | Help text for the section | [optional] 
**immutable_after_registration** | **bool** | Whether the fields in this section become read-only once the property reaches REGISTERED status. The registration section is true; post-registration customization sections are false. | [default to False]
**order** | **int** | Display order (lower first) | [optional] [default to 0]

## Example

```python
from cloudbeds_fiscal_document.models.rules_section import RulesSection

# TODO update the JSON string below
json = "{}"
# create an instance of RulesSection from a JSON string
rules_section_instance = RulesSection.from_json(json)
# print the JSON string representation of the object
print(RulesSection.to_json())

# convert the object into a dict
rules_section_dict = rules_section_instance.to_dict()
# create an instance of RulesSection from a dict
rules_section_from_dict = RulesSection.from_dict(rules_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


