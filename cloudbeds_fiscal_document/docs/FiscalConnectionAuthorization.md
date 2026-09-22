# FiscalConnectionAuthorization

Browser redirect for partner consent, present only for OAuth-handoff providers. The url is relative to the property's MFD origin — the FE prefixes window.location.origin before redirecting. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_authorization import FiscalConnectionAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionAuthorization from a JSON string
fiscal_connection_authorization_instance = FiscalConnectionAuthorization.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionAuthorization.to_json())

# convert the object into a dict
fiscal_connection_authorization_dict = fiscal_connection_authorization_instance.to_dict()
# create an instance of FiscalConnectionAuthorization from a dict
fiscal_connection_authorization_from_dict = FiscalConnectionAuthorization.from_dict(fiscal_connection_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


