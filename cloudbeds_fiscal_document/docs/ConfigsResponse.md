# ConfigsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** |  | [optional] 
**document_kind** | [**FiscalDocumentKind**](FiscalDocumentKind.md) |  | [optional] 
**show_detailed_tax_fee** | **bool** |  | [optional] 
**show_credit_notes_and_receipts** | **bool** |  | [optional] 
**charge_breakdown** | **bool** |  | [optional] 
**use_guest_lang** | **bool** |  | [optional] 
**due_days** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**legal_company_name** | **str** |  | [optional] 
**title** | **Dict[str, str]** |  | [optional] 
**show_legal_company_name** | **bool** |  | [optional] 
**include_room_number** | **bool** |  | [optional] 
**use_document_number** | **bool** |  | [optional] 
**is_compact** | **bool** |  | [optional] 
**tax_id1** | **str** |  | [optional] 
**tax_id2** | **str** |  | [optional] 
**cpf** | **str** |  | [optional] 
**custom_text** | **Dict[str, str]** |  | [optional] 
**create_invoice_on_allocation** | **bool** |  | [optional] [default to False]
**trigger_events** | [**List[DocumentTriggerEvent]**](DocumentTriggerEvent.md) |  | [optional] 
**update_invoice_on_link_document** | **bool** |  | [optional] [default to False]
**use_invoice_document_settings** | **bool** |  | [optional] [default to False]
**use_invoice_title_and_numbering** | **bool** |  | [optional] [default to False]

## Example

```python
from cloudbeds_fiscal_document.models.configs_response import ConfigsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigsResponse from a JSON string
configs_response_instance = ConfigsResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigsResponse.to_json())

# convert the object into a dict
configs_response_dict = configs_response_instance.to_dict()
# create an instance of ConfigsResponse from a dict
configs_response_from_dict = ConfigsResponse.from_dict(configs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


