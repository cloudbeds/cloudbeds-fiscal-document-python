# FiscalizationRegistrationResponse


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
**property_id** | **int** | Property ID this registration belongs to | 
**status** | [**FiscalizationRegistrationStatus**](FiscalizationRegistrationStatus.md) |  | 
**provider_id** | **str** | Provider-specific ID (e.g., Invopop party ID) | [optional] 
**is_default** | **bool** | Whether this is the default fiscalization registration | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_registration_response import FiscalizationRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationRegistrationResponse from a JSON string
fiscalization_registration_response_instance = FiscalizationRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalizationRegistrationResponse.to_json())

# convert the object into a dict
fiscalization_registration_response_dict = fiscalization_registration_response_instance.to_dict()
# create an instance of FiscalizationRegistrationResponse from a dict
fiscalization_registration_response_from_dict = FiscalizationRegistrationResponse.from_dict(fiscalization_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


