# PaymentMethodRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**CountryInfo**](CountryInfo.md) |  | 
**payment_methods** | [**List[PaymentMethodRule]**](PaymentMethodRule.md) | Available GOBL payment means keys for this country | 

## Example

```python
from cloudbeds_fiscal_document.models.payment_method_rules_response import PaymentMethodRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRulesResponse from a JSON string
payment_method_rules_response_instance = PaymentMethodRulesResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRulesResponse.to_json())

# convert the object into a dict
payment_method_rules_response_dict = payment_method_rules_response_instance.to_dict()
# create an instance of PaymentMethodRulesResponse from a dict
payment_method_rules_response_from_dict = PaymentMethodRulesResponse.from_dict(payment_method_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


