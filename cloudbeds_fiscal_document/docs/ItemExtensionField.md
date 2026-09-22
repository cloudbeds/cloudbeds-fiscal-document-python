# ItemExtensionField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | GOBL extension key (e.g., br-nfse-service, mx-cfdi-prod-serv) | 
**label** | **str** | Human-readable label for the extension field | 
**description** | **str** | Help text for the UI | [optional] 
**required** | **bool** | Whether this extension is mandatory on every line item | 
**validation_pattern** | **str** | Regex pattern for input validation (null for no validation) | [optional] 
**options** | **Dict[str, str]** | Fixed value options as label-to-value map for select fields. Null for free-text input fields. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.item_extension_field import ItemExtensionField

# TODO update the JSON string below
json = "{}"
# create an instance of ItemExtensionField from a JSON string
item_extension_field_instance = ItemExtensionField.from_json(json)
# print the JSON string representation of the object
print(ItemExtensionField.to_json())

# convert the object into a dict
item_extension_field_dict = item_extension_field_instance.to_dict()
# create an instance of ItemExtensionField from a dict
item_extension_field_from_dict = ItemExtensionField.from_dict(item_extension_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


