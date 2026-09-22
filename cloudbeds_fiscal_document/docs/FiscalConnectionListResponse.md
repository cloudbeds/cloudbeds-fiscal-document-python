# FiscalConnectionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[FiscalConnection]**](FiscalConnection.md) |  | 
**drafts** | [**List[FiscalConnectionDraft]**](FiscalConnectionDraft.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_list_response import FiscalConnectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionListResponse from a JSON string
fiscal_connection_list_response_instance = FiscalConnectionListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionListResponse.to_json())

# convert the object into a dict
fiscal_connection_list_response_dict = fiscal_connection_list_response_instance.to_dict()
# create an instance of FiscalConnectionListResponse from a dict
fiscal_connection_list_response_from_dict = FiscalConnectionListResponse.from_dict(fiscal_connection_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


