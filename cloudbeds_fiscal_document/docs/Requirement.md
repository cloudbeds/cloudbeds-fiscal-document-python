# Requirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | Whether this step is required for this country | 
**description** | **str** | Human-readable description of what this step involves | [optional] 
**fields** | [**List[RequirementField]**](RequirementField.md) | Field definitions for the UI form (only present when the step has configurable fields) | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.requirement import Requirement

# TODO update the JSON string below
json = "{}"
# create an instance of Requirement from a JSON string
requirement_instance = Requirement.from_json(json)
# print the JSON string representation of the object
print(Requirement.to_json())

# convert the object into a dict
requirement_dict = requirement_instance.to_dict()
# create an instance of Requirement from a dict
requirement_from_dict = Requirement.from_dict(requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


