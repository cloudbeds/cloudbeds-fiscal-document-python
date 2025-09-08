# LinkedDocument

Information about a document linked to another fiscal document (parent or child relationship)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the linked document | [optional] 
**number** | **str** | Number of the linked document | [optional] 
**created_at** | **datetime** | Creation date of the linked document | [optional] 
**kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 
**is_latest** | **bool** | Whether this is the latest document in the chain | [optional] 
**relationship_type** | **str** | The relationship type - PARENT means this document is linked to the current document, CHILD means the current document is linked to this one | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.linked_document import LinkedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedDocument from a JSON string
linked_document_instance = LinkedDocument.from_json(json)
# print the JSON string representation of the object
print(LinkedDocument.to_json())

# convert the object into a dict
linked_document_dict = linked_document_instance.to_dict()
# create an instance of LinkedDocument from a dict
linked_document_from_dict = LinkedDocument.from_dict(linked_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


