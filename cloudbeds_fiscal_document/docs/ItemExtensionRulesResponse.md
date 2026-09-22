# ItemExtensionRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryInfo**](CountryInfo.md) |  | 
**categories** | [**List[ItemCategoryRequirement]**](ItemCategoryRequirement.md) | Item categories that need GOBL extension mappings | 

## Example

```python
from cloudbeds_fiscal_document.models.item_extension_rules_response import ItemExtensionRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemExtensionRulesResponse from a JSON string
item_extension_rules_response_instance = ItemExtensionRulesResponse.from_json(json)
# print the JSON string representation of the object
print(ItemExtensionRulesResponse.to_json())

# convert the object into a dict
item_extension_rules_response_dict = item_extension_rules_response_instance.to_dict()
# create an instance of ItemExtensionRulesResponse from a dict
item_extension_rules_response_from_dict = ItemExtensionRulesResponse.from_dict(item_extension_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


