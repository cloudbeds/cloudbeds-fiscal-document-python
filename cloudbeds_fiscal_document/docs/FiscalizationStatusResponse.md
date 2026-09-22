# FiscalizationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** |  | 
**active** | **int** |  | [optional] 
**flows** | [**List[FiscalizationFlowStatus]**](FiscalizationFlowStatus.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_status_response import FiscalizationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationStatusResponse from a JSON string
fiscalization_status_response_instance = FiscalizationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationStatusResponse.to_json())

# convert the object into a dict
fiscalization_status_response_dict = fiscalization_status_response_instance.to_dict()
# create an instance of FiscalizationStatusResponse from a dict
fiscalization_status_response_from_dict = FiscalizationStatusResponse.from_dict(fiscalization_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


