# RecipientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the recipient. | 
**id** | **int** | ID of the recipient, references guestId, contactId, groupId, etc. depending on type. | 
**tax_document_source** | **str** | Source of the tax document number. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.recipient_request import RecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientRequest from a JSON string
recipient_request_instance = RecipientRequest.from_json(json)
# print the JSON string representation of the object
print(RecipientRequest.to_json())

# convert the object into a dict
recipient_request_dict = recipient_request_instance.to_dict()
# create an instance of RecipientRequest from a dict
recipient_request_from_dict = RecipientRequest.from_dict(recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


