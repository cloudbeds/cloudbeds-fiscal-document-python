# RecipientDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**issuing_country** | **str** |  | [optional] 
**issue_date** | **datetime** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.recipient_document import RecipientDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientDocument from a JSON string
recipient_document_instance = RecipientDocument.from_json(json)
# print the JSON string representation of the object
print(RecipientDocument.to_json())

# convert the object into a dict
recipient_document_dict = recipient_document_instance.to_dict()
# create an instance of RecipientDocument from a dict
recipient_document_from_dict = RecipientDocument.from_dict(recipient_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


