# FiscalizationSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[SeriesMapping]**](SeriesMapping.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_series_response import FiscalizationSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationSeriesResponse from a JSON string
fiscalization_series_response_instance = FiscalizationSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationSeriesResponse.to_json())

# convert the object into a dict
fiscalization_series_response_dict = fiscalization_series_response_instance.to_dict()
# create an instance of FiscalizationSeriesResponse from a dict
fiscalization_series_response_from_dict = FiscalizationSeriesResponse.from_dict(fiscalization_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


