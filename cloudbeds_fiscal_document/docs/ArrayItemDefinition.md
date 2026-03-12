# ArrayItemDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**fields** | [**List[FieldDefinition]**](FieldDefinition.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.array_item_definition import ArrayItemDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayItemDefinition from a JSON string
array_item_definition_instance = ArrayItemDefinition.from_json(json)
# print the JSON string representation of the object
print(ArrayItemDefinition.to_json())

# convert the object into a dict
array_item_definition_dict = array_item_definition_instance.to_dict()
# create an instance of ArrayItemDefinition from a dict
array_item_definition_from_dict = ArrayItemDefinition.from_dict(array_item_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


