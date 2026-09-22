# FiscalConnectionProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**visual** | [**FiscalProviderVisual**](FiscalProviderVisual.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_provider import FiscalConnectionProvider

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionProvider from a JSON string
fiscal_connection_provider_instance = FiscalConnectionProvider.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionProvider.to_json())

# convert the object into a dict
fiscal_connection_provider_dict = fiscal_connection_provider_instance.to_dict()
# create an instance of FiscalConnectionProvider from a dict
fiscal_connection_provider_from_dict = FiscalConnectionProvider.from_dict(fiscal_connection_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


