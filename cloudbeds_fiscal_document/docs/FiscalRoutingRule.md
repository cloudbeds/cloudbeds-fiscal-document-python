# FiscalRoutingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**FiscalProviderChannel**](FiscalProviderChannel.md) |  | [optional] 
**flow** | **str** |  | 
**connection** | **int** |  | [optional] 
**enabled** | **bool** |  | 
**inherits** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_routing_rule import FiscalRoutingRule

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalRoutingRule from a JSON string
fiscal_routing_rule_instance = FiscalRoutingRule.from_json(json)
# print the JSON string representation of the object
print(FiscalRoutingRule.to_json())

# convert the object into a dict
fiscal_routing_rule_dict = fiscal_routing_rule_instance.to_dict()
# create an instance of FiscalRoutingRule from a dict
fiscal_routing_rule_from_dict = FiscalRoutingRule.from_dict(fiscal_routing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


