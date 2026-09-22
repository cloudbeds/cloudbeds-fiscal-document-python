# CountryRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Requirement**](Requirement.md) |  | [optional] 
**certificate** | [**Requirement**](Requirement.md) |  | [optional] 
**external_authorization** | [**Requirement**](Requirement.md) |  | [optional] 
**series** | [**Requirement**](Requirement.md) |  | [optional] 
**tax_mapping** | [**Requirement**](Requirement.md) |  | [optional] 
**payment_method_mapping** | [**Requirement**](Requirement.md) |  | [optional] 
**item_mapping** | [**Requirement**](Requirement.md) |  | [optional] 
**operator_mapping** | [**Requirement**](Requirement.md) |  | [optional] 
**reports** | [**List[ReportDefinition]**](ReportDefinition.md) | Available reports for this country (e.g., SAF-T for PT) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.country_requirements import CountryRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of CountryRequirements from a JSON string
country_requirements_instance = CountryRequirements.from_json(json)
# print the JSON string representation of the object
print(CountryRequirements.to_json())

# convert the object into a dict
country_requirements_dict = country_requirements_instance.to_dict()
# create an instance of CountryRequirements from a dict
country_requirements_from_dict = CountryRequirements.from_dict(country_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


