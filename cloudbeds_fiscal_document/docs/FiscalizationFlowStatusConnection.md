# FiscalizationFlowStatusConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_flow_status_connection import FiscalizationFlowStatusConnection

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationFlowStatusConnection from a JSON string
fiscalization_flow_status_connection_instance = FiscalizationFlowStatusConnection.from_json(json)
# print the JSON string representation of the object
print(FiscalizationFlowStatusConnection.to_json())

# convert the object into a dict
fiscalization_flow_status_connection_dict = fiscalization_flow_status_connection_instance.to_dict()
# create an instance of FiscalizationFlowStatusConnection from a dict
fiscalization_flow_status_connection_from_dict = FiscalizationFlowStatusConnection.from_dict(fiscalization_flow_status_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


