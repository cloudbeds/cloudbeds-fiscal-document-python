# FiscalConnectionUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sections** | **Dict[str, object]** |  | [optional] 
**tax_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_update_request import FiscalConnectionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionUpdateRequest from a JSON string
fiscal_connection_update_request_instance = FiscalConnectionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionUpdateRequest.to_json())

# convert the object into a dict
fiscal_connection_update_request_dict = fiscal_connection_update_request_instance.to_dict()
# create an instance of FiscalConnectionUpdateRequest from a dict
fiscal_connection_update_request_from_dict = FiscalConnectionUpdateRequest.from_dict(fiscal_connection_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


