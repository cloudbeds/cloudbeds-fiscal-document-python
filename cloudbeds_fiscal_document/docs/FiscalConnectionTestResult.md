# FiscalConnectionTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**latency_ms** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**checked_at** | **datetime** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_test_result import FiscalConnectionTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionTestResult from a JSON string
fiscal_connection_test_result_instance = FiscalConnectionTestResult.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionTestResult.to_json())

# convert the object into a dict
fiscal_connection_test_result_dict = fiscal_connection_test_result_instance.to_dict()
# create an instance of FiscalConnectionTestResult from a dict
fiscal_connection_test_result_from_dict = FiscalConnectionTestResult.from_dict(fiscal_connection_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


