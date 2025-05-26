# CreateInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** |  | [optional] 
**source_id** | **int** |  | [optional] 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**property_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.create_invoice_request import CreateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequest from a JSON string
create_invoice_request_instance = CreateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequest.to_json())

# convert the object into a dict
create_invoice_request_dict = create_invoice_request_instance.to_dict()
# create an instance of CreateInvoiceRequest from a dict
create_invoice_request_from_dict = CreateInvoiceRequest.from_dict(create_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


