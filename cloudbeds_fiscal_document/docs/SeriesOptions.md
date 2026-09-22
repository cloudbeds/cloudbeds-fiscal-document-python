# SeriesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix_with_document_type** | **bool** | Whether the document type prefix is prepended to the series name | [optional] 
**requires_series_type** | **bool** | Whether this country requires series type selection (N/F/R) | [optional] 
**show_validation_code** | **bool** | Whether to display the validation code (e.g. AT ATCUD) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.series_options import SeriesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesOptions from a JSON string
series_options_instance = SeriesOptions.from_json(json)
# print the JSON string representation of the object
print(SeriesOptions.to_json())

# convert the object into a dict
series_options_dict = series_options_instance.to_dict()
# create an instance of SeriesOptions from a dict
series_options_from_dict = SeriesOptions.from_dict(series_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


