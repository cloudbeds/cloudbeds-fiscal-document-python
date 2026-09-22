# FiscalConnectionDraft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**current_step** | **int** | Zero-based index of the step the user was on when they saved. | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_draft import FiscalConnectionDraft

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionDraft from a JSON string
fiscal_connection_draft_instance = FiscalConnectionDraft.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionDraft.to_json())

# convert the object into a dict
fiscal_connection_draft_dict = fiscal_connection_draft_instance.to_dict()
# create an instance of FiscalConnectionDraft from a dict
fiscal_connection_draft_from_dict = FiscalConnectionDraft.from_dict(fiscal_connection_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


