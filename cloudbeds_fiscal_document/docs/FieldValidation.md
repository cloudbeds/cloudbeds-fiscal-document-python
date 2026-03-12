# FieldValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** | Regex pattern for validation | [optional] 
**min** | **int** | Minimum length or items | [optional] 
**max** | **int** | Maximum length | [optional] 
**checksum** | **bool** | Whether field has checksum validation | [optional] 
**format** | **str** | Display format mask (e.g., XX.XXX.XXX/XXXX-XX) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.field_validation import FieldValidation

# TODO update the JSON string below
json = "{}"
# create an instance of FieldValidation from a JSON string
field_validation_instance = FieldValidation.from_json(json)
# print the JSON string representation of the object
print(FieldValidation.to_json())

# convert the object into a dict
field_validation_dict = field_validation_instance.to_dict()
# create an instance of FieldValidation from a dict
field_validation_from_dict = FieldValidation.from_dict(field_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


