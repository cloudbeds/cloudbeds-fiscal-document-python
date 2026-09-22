# FiscalizationRegistrationRequest

Provider-agnostic supplier registration data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **int** | Optional scope to a specific partner instance on a multi-partner property. Omit on single-partner properties (legacy behavior).  | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country code | 
**name** | **str** | Legal name of the company | 
**tax_id** | **str** | Primary tax identification number | [optional] 
**addresses** | [**List[FiscalizationAddress]**](FiscalizationAddress.md) |  | [optional] 
**emails** | [**List[FiscalizationEmail]**](FiscalizationEmail.md) |  | [optional] 
**phones** | [**List[FiscalizationPhone]**](FiscalizationPhone.md) |  | [optional] 
**identities** | **Dict[str, str]** | Additional tax/legal identities (key-value pairs) | [optional] 
**extensions** | **Dict[str, str]** | Country-specific tax configuration. Known MX keys: &#x60;mx_border_zone&#x60; (\&quot;true\&quot;/\&quot;false\&quot;) — set to \&quot;true\&quot; for properties in Mexico&#39;s northern border zone where IVA is 8% instead of 16%.  | [optional] 

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


