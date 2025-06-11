# ConfigsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_detailed_tax_fee** | **bool** |  | 
**charge_breakdown** | **bool** |  | 
**use_guest_lang** | **bool** |  | 
**due_days** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**legal_company_name** | **str** |  | [optional] 
**title** | **Dict[str, str]** |  | [optional] 
**show_legal_company_name** | **bool** |  | 
**include_room_number** | **bool** |  | 
**use_document_number** | **bool** |  | 
**is_compact** | **bool** |  | 
**tax_id1** | **str** |  | [optional] 
**tax_id2** | **str** |  | [optional] 
**cpf** | **str** |  | [optional] 
**custom_text** | **Dict[str, str]** |  | [optional] 

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


