# ConfigsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_events** | [**List[DocumentTriggerEvent]**](DocumentTriggerEvent.md) |  | [optional] 
**show_detailed_tax_fee** | **bool** |  | 
**charge_breakdown** | **bool** |  | 
**allow_pending_transactions** | **bool** |  | [optional] 
**use_guest_lang** | **bool** |  | 
**due_days** | **int** |  | [optional] [default to 0]
**sequence_start_number** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**separator** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**legal_company_name** | **str** |  | [optional] 
**title** | **Dict[str, str]** |  | [optional] 
**show_legal_company_name** | **bool** | Show the company block (legal company name, tax IDs, registered legal address). | [default to False]
**show_property_details** | **bool** | Show the property block. Keep optional (never &#x60;required&#x60;): when omitted the stored value is preserved (a brand-new config defaults to true). At least one of the two blocks must show.  | [optional] 
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
**company_country** | **str** | Registered legal address country (ISO code). Part of the company block. | [optional] 
**company_address** | **str** | Registered legal address street. Part of the company block. | [optional] 
**company_state** | **str** | Registered legal address state/province. Part of the company block. | [optional] 
**company_city** | **str** | Registered legal address city. Part of the company block. | [optional] 
**company_post_code** | **str** | Registered legal address post code. Part of the company block. | [optional] 
**custom_text** | **Dict[str, str]** |  | [optional] 
**logo_id** | **int** |  | [optional] 
**date_display** | [**DateDisplay**](DateDisplay.md) |  | [optional] [default to DateDisplay.TRANSACTION_DATE]
**line_grouping_settings** | [**LineGroupingSettings**](LineGroupingSettings.md) |  | [optional] 
**simplified_enabled** | **bool** | Whether simplified invoices are enabled for this property (INVOICE kind). When true, simplifiedThreshold (unless the country enforces one) and simplifiedThresholdAction are required.  | [optional] 
**simplified_threshold** | **float** | Simplified-invoice monetary threshold in the property currency (INVOICE kind). Optional; required when enabled and the threshold is editable. Silently ignored rather than rejected where the country fixes the threshold itself (simplifiedThresholdEditable false) or does not support simplified invoices at all, because in those cases there is nothing to store. Must not exceed simplifiedThresholdMax when one is returned; a higher value is rejected with 400.  | [optional] 
**simplified_threshold_action** | **str** | Behaviour when a transaction total exceeds the simplified-invoice threshold (INVOICE kind). Optional; required when enabled.  | [optional] 

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


