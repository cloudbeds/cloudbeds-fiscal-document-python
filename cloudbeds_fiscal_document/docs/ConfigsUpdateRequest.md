# ConfigsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_events** | [**List[DocumentTriggerEvent]**](DocumentTriggerEvent.md) |  | [optional] 
**show_detailed_tax_fee** | **bool** |  | 
**charge_breakdown** | **bool** |  | 
**allow_pending_transactions** | **bool** |  | [optional] [default to False]
**use_guest_lang** | **bool** |  | 
**due_days** | **int** |  | [optional] [default to 0]
**sequence_start_number** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**separator** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**legal_company_name** | **str** |  | [optional] 
**title** | **Dict[str, str]** |  | [optional] 
**show_legal_company_name** | **bool** |  | [default to False]
**include_room_number** | **bool** |  | [default to False]
**use_document_number** | **bool** |  | 
**update_invoice_on_link_document** | **bool** |  | [optional] [default to False]
**is_compact** | **bool** |  | [default to False]
**use_invoice_title_and_numbering** | **bool** | Flag to determine if invoice title, sequenceStartNumber, prefix and suffix should be used. | [optional] [default to False]
**use_invoice_document_settings** | **bool** | Flag to determine if invoice document settings should be used. | [optional] [default to False]
**show_credit_notes_and_receipts** | **bool** | Flag to determine if linked credit notes and receipts should be rendered in Invoice. | [optional] [default to False]
**tax_id1** | **str** |  | [optional] 
**tax_id2** | **str** |  | [optional] 
**cpf** | **str** |  | [optional] 
**custom_text** | **Dict[str, str]** |  | [optional] 
**logo_id** | **int** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.configs_update_request import ConfigsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigsUpdateRequest from a JSON string
configs_update_request_instance = ConfigsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigsUpdateRequest.to_json())

# convert the object into a dict
configs_update_request_dict = configs_update_request_instance.to_dict()
# create an instance of ConfigsUpdateRequest from a dict
configs_update_request_from_dict = ConfigsUpdateRequest.from_dict(configs_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


