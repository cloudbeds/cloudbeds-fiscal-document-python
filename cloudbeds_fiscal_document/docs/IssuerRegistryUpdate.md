# IssuerRegistryUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tourism_classification** | **str** | Tourism establishment classification as registered with the regional authority, e.g. \&quot;Hotel 4*\&quot;. | [optional] 
**tourism_registry_code** | **str** | Registro de Turismo code, e.g. \&quot;H/SE/01234\&quot;. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.issuer_registry_update import IssuerRegistryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IssuerRegistryUpdate from a JSON string
issuer_registry_update_instance = IssuerRegistryUpdate.from_json(json)
# print the JSON string representation of the object
print(IssuerRegistryUpdate.to_json())

# convert the object into a dict
issuer_registry_update_dict = issuer_registry_update_instance.to_dict()
# create an instance of IssuerRegistryUpdate from a dict
issuer_registry_update_from_dict = IssuerRegistryUpdate.from_dict(issuer_registry_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


