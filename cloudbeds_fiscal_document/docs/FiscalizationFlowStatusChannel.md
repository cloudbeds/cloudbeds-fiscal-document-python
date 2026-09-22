# FiscalizationFlowStatusChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_flow_status_channel import FiscalizationFlowStatusChannel

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationFlowStatusChannel from a JSON string
fiscalization_flow_status_channel_instance = FiscalizationFlowStatusChannel.from_json(json)
# print the JSON string representation of the object
print(FiscalizationFlowStatusChannel.to_json())

# convert the object into a dict
fiscalization_flow_status_channel_dict = fiscalization_flow_status_channel_instance.to_dict()
# create an instance of FiscalizationFlowStatusChannel from a dict
fiscalization_flow_status_channel_from_dict = FiscalizationFlowStatusChannel.from_dict(fiscalization_flow_status_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


