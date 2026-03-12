# FieldData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placeholder** | **str** | Input placeholder text | [optional] 
**help** | **str** | Help text for the field | [optional] 
**alternatives** | **List[str]** | Alternative accepted formats (e.g., CPF for CNPJ fields) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.field_data import FieldData

# TODO update the JSON string below
json = "{}"
# create an instance of FieldData from a JSON string
field_data_instance = FieldData.from_json(json)
# print the JSON string representation of the object
print(FieldData.to_json())

# convert the object into a dict
field_data_dict = field_data_instance.to_dict()
# create an instance of FieldData from a dict
field_data_from_dict = FieldData.from_dict(field_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


