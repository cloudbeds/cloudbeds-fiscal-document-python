# ProviderOptionsReplaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**section_key** | **str** |  | 
**connection_id** | **int** |  | [optional] 
**count** | **int** | Number of options now offered in this scope. | 

## Example

```python
from cloudbeds_fiscal_document.models.provider_options_replace_response import ProviderOptionsReplaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderOptionsReplaceResponse from a JSON string
provider_options_replace_response_instance = ProviderOptionsReplaceResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderOptionsReplaceResponse.to_json())

# convert the object into a dict
provider_options_replace_response_dict = provider_options_replace_response_instance.to_dict()
# create an instance of ProviderOptionsReplaceResponse from a dict
provider_options_replace_response_from_dict = ProviderOptionsReplaceResponse.from_dict(provider_options_replace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


