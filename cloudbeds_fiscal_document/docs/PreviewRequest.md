# PreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**recipient_type** | [**RecipientType**](RecipientType.md) |  | [optional] 
**include_vat** | **bool** | Include VAT tax breakdown section in preview | [optional] [default to False]
**include_payments** | **bool** | Include payment transactions section in preview | [optional] [default to True]
**include_room_number** | **bool** | Include room number column in reservation previews | [optional] [default to True]
**preview_watermark** | **bool** | Show preview watermark on the document | [optional] [default to True]

## Example

```python
from cloudbeds_fiscal_document.models.preview_request import PreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewRequest from a JSON string
preview_request_instance = PreviewRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewRequest.to_json())

# convert the object into a dict
preview_request_dict = preview_request_instance.to_dict()
# create an instance of PreviewRequest from a dict
preview_request_from_dict = PreviewRequest.from_dict(preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


