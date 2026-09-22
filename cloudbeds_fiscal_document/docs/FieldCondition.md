# FieldCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Path of the sibling field whose value is tested (e.g. \&quot;taxId\&quot;). | 
**pattern** | **str** | Regex applied to the referenced field&#39;s value. The owning field is required only when the referenced value matches this pattern. | 

## Example

```python
from cloudbeds_fiscal_document.models.field_condition import FieldCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldCondition from a JSON string
field_condition_instance = FieldCondition.from_json(json)
# print the JSON string representation of the object
print(FieldCondition.to_json())

# convert the object into a dict
field_condition_dict = field_condition_instance.to_dict()
# create an instance of FieldCondition from a dict
field_condition_from_dict = FieldCondition.from_dict(field_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


