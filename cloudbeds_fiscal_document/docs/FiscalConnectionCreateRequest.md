# FiscalConnectionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**consent_token** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_create_request import FiscalConnectionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionCreateRequest from a JSON string
fiscal_connection_create_request_instance = FiscalConnectionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionCreateRequest.to_json())

# convert the object into a dict
fiscal_connection_create_request_dict = fiscal_connection_create_request_instance.to_dict()
# create an instance of FiscalConnectionCreateRequest from a dict
fiscal_connection_create_request_from_dict = FiscalConnectionCreateRequest.from_dict(fiscal_connection_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


