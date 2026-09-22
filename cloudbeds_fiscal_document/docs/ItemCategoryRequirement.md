# ItemCategoryRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category identifier (e.g., room_booking, item_service) | 
**label** | **str** | Human-readable label for the category | 
**single_default** | **bool** | If true, one mapping applies to all items in this category (e.g., all room bookings share the same service code) | 
**extensions** | [**List[ItemExtensionField]**](ItemExtensionField.md) | Extension fields required for items in this category | 

## Example

```python
from cloudbeds_fiscal_document.models.item_category_requirement import ItemCategoryRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategoryRequirement from a JSON string
item_category_requirement_instance = ItemCategoryRequirement.from_json(json)
# print the JSON string representation of the object
print(ItemCategoryRequirement.to_json())

# convert the object into a dict
item_category_requirement_dict = item_category_requirement_instance.to_dict()
# create an instance of ItemCategoryRequirement from a dict
item_category_requirement_from_dict = ItemCategoryRequirement.from_dict(item_category_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


