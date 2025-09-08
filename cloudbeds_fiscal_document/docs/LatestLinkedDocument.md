# LatestLinkedDocument

Information about the latest document in a rectification chain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the latest linked document | [optional] 
**number** | **str** | Number of the latest linked document | [optional] 
**created_at** | **datetime** | Creation date of the latest linked document | [optional] 
**kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**status** | [**FiscalDocumentStatus**](FiscalDocumentStatus.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.latest_linked_document import LatestLinkedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of LatestLinkedDocument from a JSON string
latest_linked_document_instance = LatestLinkedDocument.from_json(json)
# print the JSON string representation of the object
print(LatestLinkedDocument.to_json())

# convert the object into a dict
latest_linked_document_dict = latest_linked_document_instance.to_dict()
# create an instance of LatestLinkedDocument from a dict
latest_linked_document_from_dict = LatestLinkedDocument.from_dict(latest_linked_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


