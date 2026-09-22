# PaymentMethodRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Identifier to store against a mapping and send back on save. Composed by this service: the GOBL key, suffixed \&quot;::&lt;ext&gt;\&quot; when the option carries an extension code, or the partner&#39;s own code for a provider-supplied option. | 
**label** | **str** | Display text for the option; same as name for country-defined options. | 
**key** | **str** | GOBL payment means key (e.g., cash, card, credit-transfer) | 
**name** | **str** | Display name (e.g., \&quot;Cash (NU)\&quot;) | 
**ext** | **str** | Country-specific extension code override. Required when key is \&quot;other\&quot; and the country has unmapped payment codes (e.g., \&quot;MB\&quot; for Multibanco in PT). | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.payment_method_rule import PaymentMethodRule

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRule from a JSON string
payment_method_rule_instance = PaymentMethodRule.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRule.to_json())

# convert the object into a dict
payment_method_rule_dict = payment_method_rule_instance.to_dict()
# create an instance of PaymentMethodRule from a dict
payment_method_rule_from_dict = PaymentMethodRule.from_dict(payment_method_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


