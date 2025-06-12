# RecipientContactDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**cell_phone** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.recipient_contact_details import RecipientContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientContactDetails from a JSON string
recipient_contact_details_instance = RecipientContactDetails.from_json(json)
# print the JSON string representation of the object
print(RecipientContactDetails.to_json())

# convert the object into a dict
recipient_contact_details_dict = recipient_contact_details_instance.to_dict()
# create an instance of RecipientContactDetails from a dict
recipient_contact_details_from_dict = RecipientContactDetails.from_dict(recipient_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


