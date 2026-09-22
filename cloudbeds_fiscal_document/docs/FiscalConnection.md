# FiscalConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 
**detail** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**connected_at** | **datetime** |  | 
**paused_at** | **datetime** |  | [optional] 
**authorization** | [**FiscalConnectionAuthorization**](FiscalConnectionAuthorization.md) |  | [optional] 
**provider** | [**FiscalConnectionProvider**](FiscalConnectionProvider.md) |  | 
**channel** | [**FiscalConnectionChannel**](FiscalConnectionChannel.md) |  | 
**onboarding** | [**FiscalConnectionOnboarding**](FiscalConnectionOnboarding.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalConnection from a JSON string
fiscal_connection_instance = FiscalConnection.from_json(json)
# print the JSON string representation of the object
print(FiscalConnection.to_json())

# convert the object into a dict
fiscal_connection_dict = fiscal_connection_instance.to_dict()
# create an instance of FiscalConnection from a dict
fiscal_connection_from_dict = FiscalConnection.from_dict(fiscal_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


