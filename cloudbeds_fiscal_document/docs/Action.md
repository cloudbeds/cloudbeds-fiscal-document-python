# Action


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DocumentAction**](DocumentAction.md) |  | [optional] 
**fields** | [**List[FieldDefinition]**](FieldDefinition.md) | Action-specific input fields the UI must collect before submitting. Uses the same FieldDefinition schema as /fiscalization/rules.  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


