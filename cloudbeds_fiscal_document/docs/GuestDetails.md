# GuestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.guest_details import GuestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GuestDetails from a JSON string
guest_details_instance = GuestDetails.from_json(json)
# print the JSON string representation of the object
print(GuestDetails.to_json())

# convert the object into a dict
guest_details_dict = guest_details_instance.to_dict()
# create an instance of GuestDetails from a dict
guest_details_from_dict = GuestDetails.from_dict(guest_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


