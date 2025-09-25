# RecipientCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_id_type** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.recipient_company import RecipientCompany

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientCompany from a JSON string
recipient_company_instance = RecipientCompany.from_json(json)
# print the JSON string representation of the object
print(RecipientCompany.to_json())

# convert the object into a dict
recipient_company_dict = recipient_company_instance.to_dict()
# create an instance of RecipientCompany from a dict
recipient_company_from_dict = RecipientCompany.from_dict(recipient_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


