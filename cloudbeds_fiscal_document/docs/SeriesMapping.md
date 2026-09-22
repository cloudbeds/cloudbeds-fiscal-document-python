# SeriesMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_kind** | **str** | Document kind (e.g., INVOICE, CREDIT_NOTE, INVOICE_RECEIPT) | 
**series_name** | **str** | Registered series name (e.g., \&quot;FT CB-2026\&quot;) | 
**document_type** | **str** | SAF-T document type prefix (e.g., FT, NC) | [optional] 
**validation_code** | **str** | AT validation code for ATCUD generation | [optional] 
**active** | **bool** | Whether this series is currently active for new documents | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.series_mapping import SeriesMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesMapping from a JSON string
series_mapping_instance = SeriesMapping.from_json(json)
# print the JSON string representation of the object
print(SeriesMapping.to_json())

# convert the object into a dict
series_mapping_dict = series_mapping_instance.to_dict()
# create an instance of SeriesMapping from a dict
series_mapping_from_dict = SeriesMapping.from_dict(series_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


