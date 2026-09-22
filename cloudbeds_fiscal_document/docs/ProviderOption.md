# ProviderOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Stored on the mapping and echoed back to the provider unchanged. Maximum 32 characters for taxCodes and paymentMethods, 128 for series, matching their mapping columns; 255 for other sections.  | 
**label** | **str** | What the hotelier sees in the dropdown. | 
**group** | **str** | Slot within the section this option is offered for. Series are offered per document type, so send the document kind here to have the option appear only against that document. Omit for an option that applies to the whole section, which is how taxes and payment methods are offered. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.provider_option import ProviderOption

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderOption from a JSON string
provider_option_instance = ProviderOption.from_json(json)
# print the JSON string representation of the object
print(ProviderOption.to_json())

# convert the object into a dict
provider_option_dict = provider_option_instance.to_dict()
# create an instance of ProviderOption from a dict
provider_option_from_dict = ProviderOption.from_dict(provider_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


