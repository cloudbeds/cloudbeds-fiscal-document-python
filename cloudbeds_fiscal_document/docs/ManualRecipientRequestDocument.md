# ManualRecipientRequestDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GuestDocumentType**](GuestDocumentType.md) |  | [optional] 
**number** | **str** | Document number | [optional] 
**issue_date** | **date** | Document issue date | [optional] 
**issuing_country** | **str** | Country that issued the document | [optional] 
**expiration_date** | **date** | Document expiration date | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.manual_recipient_request_document import ManualRecipientRequestDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRecipientRequestDocument from a JSON string
manual_recipient_request_document_instance = ManualRecipientRequestDocument.from_json(json)
# print the JSON string representation of the object
print(ManualRecipientRequestDocument.to_json())

# convert the object into a dict
manual_recipient_request_document_dict = manual_recipient_request_document_instance.to_dict()
# create an instance of ManualRecipientRequestDocument from a dict
manual_recipient_request_document_from_dict = ManualRecipientRequestDocument.from_dict(manual_recipient_request_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


