# FiscalProviderListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[FiscalProvider]**](FiscalProvider.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_provider_list_response import FiscalProviderListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalProviderListResponse from a JSON string
fiscal_provider_list_response_instance = FiscalProviderListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalProviderListResponse.to_json())

# convert the object into a dict
fiscal_provider_list_response_dict = fiscal_provider_list_response_instance.to_dict()
# create an instance of FiscalProviderListResponse from a dict
fiscal_provider_list_response_from_dict = FiscalProviderListResponse.from_dict(fiscal_provider_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


