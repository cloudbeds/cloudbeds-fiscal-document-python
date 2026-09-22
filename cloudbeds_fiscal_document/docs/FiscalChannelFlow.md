# FiscalChannelFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**inherits** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_channel_flow import FiscalChannelFlow

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalChannelFlow from a JSON string
fiscal_channel_flow_instance = FiscalChannelFlow.from_json(json)
# print the JSON string representation of the object
print(FiscalChannelFlow.to_json())

# convert the object into a dict
fiscal_channel_flow_dict = fiscal_channel_flow_instance.to_dict()
# create an instance of FiscalChannelFlow from a dict
fiscal_channel_flow_from_dict = FiscalChannelFlow.from_dict(fiscal_channel_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


