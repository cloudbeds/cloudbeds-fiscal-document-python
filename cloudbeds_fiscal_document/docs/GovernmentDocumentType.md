# GovernmentDocumentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Government document identifier (e.g. NFSE, NFCE) | 
**name** | **str** | Display name (e.g. NFS-e, NFC-e) | 

## Example

```python
from cloudbeds_fiscal_document.models.government_document_type import GovernmentDocumentType

# TODO update the JSON string below
json = "{}"
# create an instance of GovernmentDocumentType from a JSON string
government_document_type_instance = GovernmentDocumentType.from_json(json)
# print the JSON string representation of the object
print(GovernmentDocumentType.to_json())

# convert the object into a dict
government_document_type_dict = government_document_type_instance.to_dict()
# create an instance of GovernmentDocumentType from a dict
government_document_type_from_dict = GovernmentDocumentType.from_dict(government_document_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


