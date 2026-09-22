# FiscalConnectionChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | [optional] 
**flows** | [**List[FiscalChannelFlow]**](FiscalChannelFlow.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection_channel import FiscalConnectionChannel

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnectionChannel from a JSON string
fiscal_connection_channel_instance = FiscalConnectionChannel.from_json(json)
# print the JSON string representation of the object
print(FiscalConnectionChannel.to_json())

# convert the object into a dict
fiscal_connection_channel_dict = fiscal_connection_channel_instance.to_dict()
# create an instance of FiscalConnectionChannel from a dict
fiscal_connection_channel_from_dict = FiscalConnectionChannel.from_dict(fiscal_connection_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


