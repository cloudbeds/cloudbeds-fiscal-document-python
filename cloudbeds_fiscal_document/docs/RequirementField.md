# RequirementField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name used in the API request | 
**type** | **str** | Field input type | 
**required** | **bool** | Whether this field is required | [optional] [default to False]
**label** | **str** | Display label for the field | [optional] 
**description** | **str** | Help text or description for the field | [optional] 
**accept** | **str** | Accepted file types (for file fields, e.g., \&quot;.p12,.pfx,.pem\&quot;) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.requirement_field import RequirementField

# TODO update the JSON string below
json = "{}"
# create an instance of RequirementField from a JSON string
requirement_field_instance = RequirementField.from_json(json)
# print the JSON string representation of the object
print(RequirementField.to_json())

# convert the object into a dict
requirement_field_dict = requirement_field_instance.to_dict()
# create an instance of RequirementField from a dict
requirement_field_from_dict = RequirementField.from_dict(requirement_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


