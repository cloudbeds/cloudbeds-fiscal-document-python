# FiscalProviderChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_provider_channel import FiscalProviderChannel

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalProviderChannel from a JSON string
fiscal_provider_channel_instance = FiscalProviderChannel.from_json(json)
# print the JSON string representation of the object
print(FiscalProviderChannel.to_json())

# convert the object into a dict
fiscal_provider_channel_dict = fiscal_provider_channel_instance.to_dict()
# create an instance of FiscalProviderChannel from a dict
fiscal_provider_channel_from_dict = FiscalProviderChannel.from_dict(fiscal_provider_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


