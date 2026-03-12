# FiscalizationPhone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Phone number (international format preferred) | 
**label** | **str** | Optional label for the phone | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_phone import FiscalizationPhone

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationPhone from a JSON string
fiscalization_phone_instance = FiscalizationPhone.from_json(json)
# print the JSON string representation of the object
print(FiscalizationPhone.to_json())

# convert the object into a dict
fiscalization_phone_dict = fiscalization_phone_instance.to_dict()
# create an instance of FiscalizationPhone from a dict
fiscalization_phone_from_dict = FiscalizationPhone.from_dict(fiscalization_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


