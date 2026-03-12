# FieldDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Field path (e.g., \&quot;name\&quot;, \&quot;tax_id.code\&quot;, \&quot;addresses\&quot;) | 
**label** | **str** | Display label for the field | 
**type** | **str** | Field input type | 
**category** | **str** | Field grouping category | [optional] 
**required** | **bool** | Whether field is required | 
**primary** | **bool** | Indicates primary tax ID field | [optional] [default to False]
**validation** | [**FieldValidation**](FieldValidation.md) |  | [optional] 
**data** | [**FieldData**](FieldData.md) |  | [optional] 
**options** | [**List[SelectOption]**](SelectOption.md) |  | [optional] 
**item** | [**ArrayItemDefinition**](ArrayItemDefinition.md) |  | [optional] 
**properties** | [**Dict[str, FieldDefinition]**](FieldDefinition.md) | Object properties for object type fields | [optional] 
**default** | [**FieldDefinitionDefault**](FieldDefinitionDefault.md) |  | [optional] 
**description** | **str** | Field description | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.field_definition import FieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDefinition from a JSON string
field_definition_instance = FieldDefinition.from_json(json)
# print the JSON string representation of the object
print(FieldDefinition.to_json())

# convert the object into a dict
field_definition_dict = field_definition_instance.to_dict()
# create an instance of FieldDefinition from a dict
field_definition_from_dict = FieldDefinition.from_dict(field_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


