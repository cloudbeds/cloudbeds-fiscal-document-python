# FiscalizationRegistrationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | ISO 3166-1 alpha-2 country code | 
**status** | **str** | Registration status with government systems | 
**provider_id** | **str** | Provider-specific registration ID | [optional] 
**link_url** | **str** | External link URL when status is AWAITING (e.g., government portal) | [optional] 
**created_at** | **datetime** | When registration was created | [optional] 
**updated_at** | **datetime** | When status was last updated | [optional] 
**error** | **str** | Error if registration failed | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_registration_status import FiscalizationRegistrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationRegistrationStatus from a JSON string
fiscalization_registration_status_instance = FiscalizationRegistrationStatus.from_json(json)
# print the JSON string representation of the object
print(FiscalizationRegistrationStatus.to_json())

# convert the object into a dict
fiscalization_registration_status_dict = fiscalization_registration_status_instance.to_dict()
# create an instance of FiscalizationRegistrationStatus from a dict
fiscalization_registration_status_from_dict = FiscalizationRegistrationStatus.from_dict(fiscalization_registration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


