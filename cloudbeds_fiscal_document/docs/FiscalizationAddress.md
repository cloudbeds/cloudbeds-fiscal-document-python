# FiscalizationAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street address with number | 
**number** | **str** | Street number (separate field for countries like Brazil) | [optional] 
**locality** | **str** | Neighborhood or locality | [optional] 
**region** | **str** | City, region, or administrative area | [optional] 
**state** | **str** | State/Province/Region code | [optional] 
**postal_code** | **str** | Postal/ZIP code | 
**country** | **str** | ISO 3166-1 alpha-2 country code | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_address import FiscalizationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationAddress from a JSON string
fiscalization_address_instance = FiscalizationAddress.from_json(json)
# print the JSON string representation of the object
print(FiscalizationAddress.to_json())

# convert the object into a dict
fiscalization_address_dict = fiscalization_address_instance.to_dict()
# create an instance of FiscalizationAddress from a dict
fiscalization_address_from_dict = FiscalizationAddress.from_dict(fiscalization_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


