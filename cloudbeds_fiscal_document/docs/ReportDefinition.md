# ReportDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique report identifier (e.g., \&quot;saft\&quot;) | 
**label** | **str** | Display label for the report | 
**description** | **str** | Detailed description of the report | [optional] 
**params** | [**List[ReportParam]**](ReportParam.md) | Parameters the user must provide to generate the report | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.report_definition import ReportDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDefinition from a JSON string
report_definition_instance = ReportDefinition.from_json(json)
# print the JSON string representation of the object
print(ReportDefinition.to_json())

# convert the object into a dict
report_definition_dict = report_definition_instance.to_dict()
# create an instance of ReportDefinition from a dict
report_definition_from_dict = ReportDefinition.from_dict(report_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


