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
**allow_pending_transactions** | **bool** |  | [optional] 
**due_days** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**separator** | **str** |  | [optional] 
**legal_company_name** | **str** |  | [optional] 
**title** | **Dict[str, str]** |  | [optional] 
**show_legal_company_name** | **bool** |  | [optional] 
**show_property_details** | **bool** |  | [optional] 
**include_room_number** | **bool** |  | [optional] 
**use_document_number** | **bool** |  | [optional] 
**is_compact** | **bool** |  | [optional] 
**tax_id1** | **str** |  | [optional] 
**tax_id2** | **str** |  | [optional] 
**cpf** | **str** |  | [optional] 
**company_country** | **str** |  | [optional] 
**company_address** | **str** |  | [optional] 
**company_state** | **str** |  | [optional] 
**company_city** | **str** |  | [optional] 
**company_post_code** | **str** |  | [optional] 
**custom_text** | **Dict[str, str]** |  | [optional] 
**trigger_events** | [**List[DocumentTriggerEvent]**](DocumentTriggerEvent.md) |  | [optional] 
**update_invoice_on_link_document** | **bool** |  | [optional] [default to False]
**use_invoice_document_settings** | **bool** |  | [optional] [default to False]
**use_invoice_title_and_numbering** | **bool** |  | [optional] [default to False]
**date_display** | [**DateDisplay**](DateDisplay.md) |  | [optional] [default to DateDisplay.TRANSACTION_DATE]
**line_grouping_settings** | [**LineGroupingSettings**](LineGroupingSettings.md) |  | [optional] 
**simplified_supported** | **bool** | Whether simplified invoices are supported for this property&#39;s country (INVOICE kind) | [optional] 
**simplified_enabled** | **bool** | Whether simplified invoices are enabled for this property (INVOICE kind) | [optional] 
**simplified_threshold_editable** | **bool** | Whether the property may choose the simplified threshold. false means the country fixes it in regulation, so the threshold returned below is that country-fixed value: render it read-only and do not send one on save.  | [optional] 
**simplified_threshold** | **float** | Effective simplified-invoice threshold in the property currency (INVOICE kind): the country-fixed value where the country fixes one, otherwise the property-configured value. Null when not configured.  | [optional] 
**simplified_threshold_max** | **float** | Statutory ceiling for the simplified-invoice threshold in the property currency (INVOICE kind). The property may configure any amount up to this; a higher value is rejected on save. Null when the country has no legal limit (e.g. Italy) or does not support simplified invoices at all.  | [optional] 
**simplified_threshold_action** | **str** | Behaviour when the total exceeds the simplified-invoice threshold (INVOICE kind) | [optional] 

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


