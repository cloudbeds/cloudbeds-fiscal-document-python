# VoidReceiptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Cancellation reason for the fiscal authority. Required on Mexico when voiding a fiscalized payment receipt (CFDI tipo P), where it is the SAT motivo de cancelacion: \&quot;02\&quot; (issued with errors, no substitute) or \&quot;03\&quot; (operation not carried out). Defaults to \&quot;03\&quot; when omitted. Ignored by countries that do not fiscalize a receipt void.  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.void_receipt_request import VoidReceiptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidReceiptRequest from a JSON string
void_receipt_request_instance = VoidReceiptRequest.from_json(json)
# print the JSON string representation of the object
print(VoidReceiptRequest.to_json())

# convert the object into a dict
void_receipt_request_dict = void_receipt_request_instance.to_dict()
# create an instance of VoidReceiptRequest from a dict
void_receipt_request_from_dict = VoidReceiptRequest.from_dict(void_receipt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


