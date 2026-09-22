# FiscalizationFlowStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow** | [**FiscalizationFlowStatusFlow**](FiscalizationFlowStatusFlow.md) |  | 
**channel** | [**FiscalizationFlowStatusChannel**](FiscalizationFlowStatusChannel.md) |  | [optional] 
**connection** | [**FiscalizationFlowStatusConnection**](FiscalizationFlowStatusConnection.md) |  | [optional] 
**ready** | **bool** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_flow_status import FiscalizationFlowStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationFlowStatus from a JSON string
fiscalization_flow_status_instance = FiscalizationFlowStatus.from_json(json)
# print the JSON string representation of the object
print(FiscalizationFlowStatus.to_json())

# convert the object into a dict
fiscalization_flow_status_dict = fiscalization_flow_status_instance.to_dict()
# create an instance of FiscalizationFlowStatus from a dict
fiscalization_flow_status_from_dict = FiscalizationFlowStatus.from_dict(fiscalization_flow_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


