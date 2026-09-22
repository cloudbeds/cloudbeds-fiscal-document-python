# IssuerRegistryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tourism_classification** | **str** |  | [optional] 
**tourism_registry_code** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.issuer_registry_response import IssuerRegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssuerRegistryResponse from a JSON string
issuer_registry_response_instance = IssuerRegistryResponse.from_json(json)
# print the JSON string representation of the object
print(IssuerRegistryResponse.to_json())

# convert the object into a dict
issuer_registry_response_dict = issuer_registry_response_instance.to_dict()
# create an instance of IssuerRegistryResponse from a dict
issuer_registry_response_from_dict = IssuerRegistryResponse.from_dict(issuer_registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


