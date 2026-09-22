# FiscalConnectionActivateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_token** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_activate_request import FiscalConnectionActivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionActivateRequest from a JSON string
fiscal_connection_activate_request_instance = FiscalConnectionActivateRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionActivateRequest.to_json())

# convert the object into a dict
fiscal_connection_activate_request_dict = fiscal_connection_activate_request_instance.to_dict()
# create an instance of FiscalConnectionActivateRequest from a dict
fiscal_connection_activate_request_from_dict = FiscalConnectionActivateRequest.from_dict(fiscal_connection_activate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


