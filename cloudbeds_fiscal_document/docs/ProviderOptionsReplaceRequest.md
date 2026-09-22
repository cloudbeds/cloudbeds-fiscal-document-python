# ProviderOptionsReplaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** | Scope of the replacement. Omit for the provider&#39;s catalogue across every property; send a connection id when the values belong to a single customer account.  | [optional] 
**options** | [**List[ProviderOption]**](ProviderOption.md) | The full list for this scope, in display order; anything not listed is deactivated. Active options are served before retired options, with connection-scoped options before provider-wide options of the same active status.  | 

## Example

```python
from cloudbeds_fiscal_document.models.provider_options_replace_request import ProviderOptionsReplaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderOptionsReplaceRequest from a JSON string
provider_options_replace_request_instance = ProviderOptionsReplaceRequest.from_json(json)
# print the JSON string representation of the object
print(ProviderOptionsReplaceRequest.to_json())

# convert the object into a dict
provider_options_replace_request_dict = provider_options_replace_request_instance.to_dict()
# create an instance of ProviderOptionsReplaceRequest from a dict
provider_options_replace_request_from_dict = ProviderOptionsReplaceRequest.from_dict(provider_options_replace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


