# FiscalizationSeriesRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryInfo**](CountryInfo.md) |  | 
**document_types** | [**List[SeriesDocumentType]**](SeriesDocumentType.md) | Available series slots that require registration | 
**series_types** | [**List[SeriesType]**](SeriesType.md) | Available series types for this environment | 
**series_options** | [**SeriesOptions**](SeriesOptions.md) |  | [optional] 
**dimension_groups** | [**List[SeriesDimensionGroup]**](SeriesDimensionGroup.md) | Grouped series dimensions (gov doc → business types). When present, use 2-step selection. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_series_rules_response import FiscalizationSeriesRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationSeriesRulesResponse from a JSON string
fiscalization_series_rules_response_instance = FiscalizationSeriesRulesResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationSeriesRulesResponse.to_json())

# convert the object into a dict
fiscalization_series_rules_response_dict = fiscalization_series_rules_response_instance.to_dict()
# create an instance of FiscalizationSeriesRulesResponse from a dict
fiscalization_series_rules_response_from_dict = FiscalizationSeriesRulesResponse.from_dict(fiscalization_series_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


