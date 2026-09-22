# FiscalChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**flows** | [**List[FiscalChannelFlow]**](FiscalChannelFlow.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_channel import FiscalChannel

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalChannel from a JSON string
fiscal_channel_instance = FiscalChannel.from_json(json)
# print the JSON string representation of the object
print(FiscalChannel.to_json())

# convert the object into a dict
fiscal_channel_dict = fiscal_channel_instance.to_dict()
# create an instance of FiscalChannel from a dict
fiscal_channel_from_dict = FiscalChannel.from_dict(fiscal_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


