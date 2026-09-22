# FiscalProviderVisual


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bg** | **str** |  | [optional] 
**fg** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_provider_visual import FiscalProviderVisual

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalProviderVisual from a JSON string
fiscal_provider_visual_instance = FiscalProviderVisual.from_json(json)
# print the JSON string representation of the object
print(FiscalProviderVisual.to_json())

# convert the object into a dict
fiscal_provider_visual_dict = fiscal_provider_visual_instance.to_dict()
# create an instance of FiscalProviderVisual from a dict
fiscal_provider_visual_from_dict = FiscalProviderVisual.from_dict(fiscal_provider_visual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


