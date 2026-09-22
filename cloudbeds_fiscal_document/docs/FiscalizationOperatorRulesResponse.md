# FiscalizationOperatorRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryInfo**](CountryInfo.md) |  | 
**operator_required** | **bool** | Whether this country requires per-invoice operator legal-ID mapping | 
**legal_id_label** | **str** | Country-specific label for the operator legal ID (e.g., \&quot;OIB\&quot; for HR) | [optional] 
**legal_id_pattern** | **str** | Regex pattern the legal ID must match (e.g., \&quot;^\\\\d{11}$\&quot; for HR OIB) | [optional] 
**legal_id_help_text** | **str** | Helper text shown beside the legal ID input to guide the admin | [optional] 
**legal_name_max_length** | **int** | Maximum length allowed for the legal name (enforced both client and server) | [optional] 
**legal_name_help_text** | **str** | Helper text shown beside the legal name input | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_operator_rules_response import FiscalizationOperatorRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationOperatorRulesResponse from a JSON string
fiscalization_operator_rules_response_instance = FiscalizationOperatorRulesResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationOperatorRulesResponse.to_json())

# convert the object into a dict
fiscalization_operator_rules_response_dict = fiscalization_operator_rules_response_instance.to_dict()
# create an instance of FiscalizationOperatorRulesResponse from a dict
fiscalization_operator_rules_response_from_dict = FiscalizationOperatorRulesResponse.from_dict(fiscalization_operator_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


