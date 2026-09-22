# ReportParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name (used as query param) | 
**type** | **str** | Parameter input type | 
**required** | **bool** |  | 
**label** | **str** | Display label | 
**description** | **str** | Help text | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.report_param import ReportParam

# TODO update the JSON string below
json = "{}"
# create an instance of ReportParam from a JSON string
report_param_instance = ReportParam.from_json(json)
# print the JSON string representation of the object
print(ReportParam.to_json())

# convert the object into a dict
report_param_dict = report_param_instance.to_dict()
# create an instance of ReportParam from a dict
report_param_from_dict = ReportParam.from_dict(report_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


