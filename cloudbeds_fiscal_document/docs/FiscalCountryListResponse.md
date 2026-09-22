# FiscalCountryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_country_list_response import FiscalCountryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalCountryListResponse from a JSON string
fiscal_country_list_response_instance = FiscalCountryListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalCountryListResponse.to_json())

# convert the object into a dict
fiscal_country_list_response_dict = fiscal_country_list_response_instance.to_dict()
# create an instance of FiscalCountryListResponse from a dict
fiscal_country_list_response_from_dict = FiscalCountryListResponse.from_dict(fiscal_country_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


