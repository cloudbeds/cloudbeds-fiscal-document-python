# FiscalConnectionDraftUpsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 
**current_step** | **int** | Zero-based step index for resume. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_draft_upsert_request import FiscalConnectionDraftUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionDraftUpsertRequest from a JSON string
fiscal_connection_draft_upsert_request_instance = FiscalConnectionDraftUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionDraftUpsertRequest.to_json())

# convert the object into a dict
fiscal_connection_draft_upsert_request_dict = fiscal_connection_draft_upsert_request_instance.to_dict()
# create an instance of FiscalConnectionDraftUpsertRequest from a dict
fiscal_connection_draft_upsert_request_from_dict = FiscalConnectionDraftUpsertRequest.from_dict(fiscal_connection_draft_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


