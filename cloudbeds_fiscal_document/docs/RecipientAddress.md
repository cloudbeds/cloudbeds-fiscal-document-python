# RecipientAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.recipient_address import RecipientAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientAddress from a JSON string
recipient_address_instance = RecipientAddress.from_json(json)
# print the JSON string representation of the object
print(RecipientAddress.to_json())

# convert the object into a dict
recipient_address_dict = recipient_address_instance.to_dict()
# create an instance of RecipientAddress from a dict
recipient_address_from_dict = RecipientAddress.from_dict(recipient_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


