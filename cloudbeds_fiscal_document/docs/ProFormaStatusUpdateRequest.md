# ProFormaStatusUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | New status for the pro forma invoice | 

## Example

```python
from cloudbeds_fiscal_document.models.pro_forma_status_update_request import ProFormaStatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProFormaStatusUpdateRequest from a JSON string
pro_forma_status_update_request_instance = ProFormaStatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProFormaStatusUpdateRequest.to_json())

# convert the object into a dict
pro_forma_status_update_request_dict = pro_forma_status_update_request_instance.to_dict()
# create an instance of ProFormaStatusUpdateRequest from a dict
pro_forma_status_update_request_from_dict = ProFormaStatusUpdateRequest.from_dict(pro_forma_status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


