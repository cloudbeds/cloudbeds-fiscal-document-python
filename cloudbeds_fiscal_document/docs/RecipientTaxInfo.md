# RecipientTaxInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**source** | **str** | Indicates whether the tax identification used is from Tax ID or Document Number. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.recipient_tax_info import RecipientTaxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientTaxInfo from a JSON string
recipient_tax_info_instance = RecipientTaxInfo.from_json(json)
# print the JSON string representation of the object
print(RecipientTaxInfo.to_json())

# convert the object into a dict
recipient_tax_info_dict = recipient_tax_info_instance.to_dict()
# create an instance of RecipientTaxInfo from a dict
recipient_tax_info_from_dict = RecipientTaxInfo.from_dict(recipient_tax_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


