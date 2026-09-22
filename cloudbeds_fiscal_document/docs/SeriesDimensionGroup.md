# SeriesDimensionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**government_document** | [**GovernmentDocumentType**](GovernmentDocumentType.md) |  | 
**business_document_types** | [**List[SeriesDocumentType]**](SeriesDocumentType.md) | Business document types available under this government document | 
**name_validation** | [**FieldValidation**](FieldValidation.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.series_dimension_group import SeriesDimensionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesDimensionGroup from a JSON string
series_dimension_group_instance = SeriesDimensionGroup.from_json(json)
# print the JSON string representation of the object
print(SeriesDimensionGroup.to_json())

# convert the object into a dict
series_dimension_group_dict = series_dimension_group_instance.to_dict()
# create an instance of SeriesDimensionGroup from a dict
series_dimension_group_from_dict = SeriesDimensionGroup.from_dict(series_dimension_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


