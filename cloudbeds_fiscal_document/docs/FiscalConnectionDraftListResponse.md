# FiscalConnectionDraftListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drafts** | [**List[FiscalConnectionDraft]**](FiscalConnectionDraft.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_draft_list_response import FiscalConnectionDraftListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionDraftListResponse from a JSON string
fiscal_connection_draft_list_response_instance = FiscalConnectionDraftListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionDraftListResponse.to_json())

# convert the object into a dict
fiscal_connection_draft_list_response_dict = fiscal_connection_draft_list_response_instance.to_dict()
# create an instance of FiscalConnectionDraftListResponse from a dict
fiscal_connection_draft_list_response_from_dict = FiscalConnectionDraftListResponse.from_dict(fiscal_connection_draft_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


