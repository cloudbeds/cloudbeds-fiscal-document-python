# FiscalRoutingRulePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_routing_rule_patch import FiscalRoutingRulePatch

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalRoutingRulePatch from a JSON string
fiscal_routing_rule_patch_instance = FiscalRoutingRulePatch.from_json(json)
# print the JSON string representation of the object
print(FiscalRoutingRulePatch.to_json())

# convert the object into a dict
fiscal_routing_rule_patch_dict = fiscal_routing_rule_patch_instance.to_dict()
# create an instance of FiscalRoutingRulePatch from a dict
fiscal_routing_rule_patch_from_dict = FiscalRoutingRulePatch.from_dict(fiscal_routing_rule_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


