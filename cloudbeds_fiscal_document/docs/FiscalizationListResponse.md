# FiscalizationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** |  | [optional] 
**configs** | [**List[FiscalizationRegistrationResponse]**](FiscalizationRegistrationResponse.md) | List of fiscalization registrations for this property | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_list_response import FiscalizationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationListResponse from a JSON string
fiscalization_list_response_instance = FiscalizationListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationListResponse.to_json())

# convert the object into a dict
fiscalization_list_response_dict = fiscalization_list_response_instance.to_dict()
# create an instance of FiscalizationListResponse from a dict
fiscalization_list_response_from_dict = FiscalizationListResponse.from_dict(fiscalization_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


