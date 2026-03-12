# FiscalizationRegistrationRequest

Provider-agnostic supplier registration data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | ISO 3166-1 alpha-2 country code | 
**name** | **str** | Legal name of the company | 
**tax_id** | **str** | Primary tax identification number | [optional] 
**addresses** | [**List[FiscalizationAddress]**](FiscalizationAddress.md) |  | [optional] 
**emails** | [**List[FiscalizationEmail]**](FiscalizationEmail.md) |  | [optional] 
**phones** | [**List[FiscalizationPhone]**](FiscalizationPhone.md) |  | [optional] 
**identities** | **Dict[str, str]** | Additional tax/legal identities (key-value pairs) | [optional] 
**extensions** | **Dict[str, str]** | Country-specific tax configuration | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_registration_request import FiscalizationRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationRegistrationRequest from a JSON string
fiscalization_registration_request_instance = FiscalizationRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(FiscalizationRegistrationRequest.to_json())

# convert the object into a dict
fiscalization_registration_request_dict = fiscalization_registration_request_instance.to_dict()
# create an instance of FiscalizationRegistrationRequest from a dict
fiscalization_registration_request_from_dict = FiscalizationRegistrationRequest.from_dict(fiscalization_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


