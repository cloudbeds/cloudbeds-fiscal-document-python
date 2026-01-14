# ManualRecipientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of recipient (person or company) | 
**name** | **str** | Name of the recipient | 
**gender** | [**GuestGender**](GuestGender.md) |  | [optional] 
**email** | **str** | Email address of the recipient | [optional] 
**birthday** | **date** | Birthday of the recipient | [optional] 
**phone** | **str** | Phone number | [optional] 
**cell_phone** | **str** | Cell phone number | [optional] 
**tax_id** | **str** | Tax ID / VAT number | 
**address** | [**ManualRecipientRequestAddress**](ManualRecipientRequestAddress.md) |  | [optional] 
**document** | [**ManualRecipientRequestDocument**](ManualRecipientRequestDocument.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.manual_recipient_request import ManualRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRecipientRequest from a JSON string
manual_recipient_request_instance = ManualRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(ManualRecipientRequest.to_json())

# convert the object into a dict
manual_recipient_request_dict = manual_recipient_request_instance.to_dict()
# create an instance of ManualRecipientRequest from a dict
manual_recipient_request_from_dict = ManualRecipientRequest.from_dict(manual_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


