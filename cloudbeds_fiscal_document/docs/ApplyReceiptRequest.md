# ApplyReceiptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** | The ID of the invoice to apply the receipt to. | 

## Example

```python
from cloudbeds_fiscal_document.models.apply_receipt_request import ApplyReceiptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyReceiptRequest from a JSON string
apply_receipt_request_instance = ApplyReceiptRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyReceiptRequest.to_json())

# convert the object into a dict
apply_receipt_request_dict = apply_receipt_request_instance.to_dict()
# create an instance of ApplyReceiptRequest from a dict
apply_receipt_request_from_dict = ApplyReceiptRequest.from_dict(apply_receipt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


