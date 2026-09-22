# SeriesType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Series type code (N, F, R) | 
**name** | **str** | Series type name (e.g., Normal, Training, Recovery) | 
**description** | **str** | Description of the series type | 

## Example

```python
from cloudbeds_fiscal_document.models.series_type import SeriesType

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesType from a JSON string
series_type_instance = SeriesType.from_json(json)
# print the JSON string representation of the object
print(SeriesType.to_json())

# convert the object into a dict
series_type_dict = series_type_instance.to_dict()
# create an instance of SeriesType from a dict
series_type_from_dict = SeriesType.from_dict(series_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


