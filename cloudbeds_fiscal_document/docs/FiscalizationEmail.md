# FiscalizationEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Email address | 
**label** | **str** | Optional label for the email | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscalization_email import FiscalizationEmail

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalizationEmail from a JSON string
fiscalization_email_instance = FiscalizationEmail.from_json(json)
# print the JSON string representation of the object
print(FiscalizationEmail.to_json())

# convert the object into a dict
fiscalization_email_dict = fiscalization_email_instance.to_dict()
# create an instance of FiscalizationEmail from a dict
fiscalization_email_from_dict = FiscalizationEmail.from_dict(fiscalization_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


