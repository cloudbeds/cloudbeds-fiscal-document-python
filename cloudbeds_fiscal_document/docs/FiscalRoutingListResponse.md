# FiscalRoutingListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing** | [**List[FiscalRoutingRule]**](FiscalRoutingRule.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_routing_list_response import FiscalRoutingListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalRoutingListResponse from a JSON string
fiscal_routing_list_response_instance = FiscalRoutingListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalRoutingListResponse.to_json())

# convert the object into a dict
fiscal_routing_list_response_dict = fiscal_routing_list_response_instance.to_dict()
# create an instance of FiscalRoutingListResponse from a dict
fiscal_routing_list_response_from_dict = FiscalRoutingListResponse.from_dict(fiscal_routing_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


