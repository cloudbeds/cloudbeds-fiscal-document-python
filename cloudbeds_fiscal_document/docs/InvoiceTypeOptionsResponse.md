# InvoiceTypeOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_type_options** | **List[str]** | Invoice classes (e.g. A/B/T) the property may choose between when issuing an invoice; empty when there is no choice to surface. | 

## Example

```python
from cloudbeds_fiscal_document.models.invoice_type_options_response import InvoiceTypeOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTypeOptionsResponse from a JSON string
invoice_type_options_response_instance = InvoiceTypeOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceTypeOptionsResponse.to_json())

# convert the object into a dict
invoice_type_options_response_dict = invoice_type_options_response_instance.to_dict()
# create an instance of InvoiceTypeOptionsResponse from a dict
invoice_type_options_response_from_dict = InvoiceTypeOptionsResponse.from_dict(invoice_type_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


