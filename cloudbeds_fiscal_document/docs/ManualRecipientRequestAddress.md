# ManualRecipientRequestAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country code | [optional] 
**state** | **str** | State or province | [optional] 
**city** | **str** | City | [optional] 
**address1** | **str** | Primary street address | [optional] 
**address2** | **str** | Secondary street address | [optional] 
**zip** | **str** | Zip/postal code | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.manual_recipient_request_address import ManualRecipientRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRecipientRequestAddress from a JSON string
manual_recipient_request_address_instance = ManualRecipientRequestAddress.from_json(json)
# print the JSON string representation of the object
print(ManualRecipientRequestAddress.to_json())

# convert the object into a dict
manual_recipient_request_address_dict = manual_recipient_request_address_instance.to_dict()
# create an instance of ManualRecipientRequestAddress from a dict
manual_recipient_request_address_from_dict = ManualRecipientRequestAddress.from_dict(manual_recipient_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


