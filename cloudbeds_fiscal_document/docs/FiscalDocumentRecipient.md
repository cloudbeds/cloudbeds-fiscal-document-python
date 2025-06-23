# FiscalDocumentRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**type** | [**RecipientType**](RecipientType.md) |  | [optional] 
**address** | [**RecipientAddress**](RecipientAddress.md) |  | [optional] 
**tax** | [**RecipientTaxInfo**](RecipientTaxInfo.md) |  | [optional] 
**contact_details** | [**RecipientContactDetails**](RecipientContactDetails.md) |  | [optional] 
**document** | [**RecipientDocument**](RecipientDocument.md) |  | [optional] 
**country_data** | **Dict[str, object]** | Arbitrary country-specific fields from guest requirements.  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_document_recipient import FiscalDocumentRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentRecipient from a JSON string
fiscal_document_recipient_instance = FiscalDocumentRecipient.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentRecipient.to_json())

# convert the object into a dict
fiscal_document_recipient_dict = fiscal_document_recipient_instance.to_dict()
# create an instance of FiscalDocumentRecipient from a dict
fiscal_document_recipient_from_dict = FiscalDocumentRecipient.from_dict(fiscal_document_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


