# FiscalizationValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the data is valid | 
**errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_validation_result import FiscalizationValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationValidationResult from a JSON string
fiscalization_validation_result_instance = FiscalizationValidationResult.from_json(json)
# print the JSON string representation of the object
print(FiscalizationValidationResult.to_json())

# convert the object into a dict
fiscalization_validation_result_dict = fiscalization_validation_result_instance.to_dict()
# create an instance of FiscalizationValidationResult from a dict
fiscalization_validation_result_from_dict = FiscalizationValidationResult.from_dict(fiscalization_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


