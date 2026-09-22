# ActivateSeriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_code** | **str** | The series code to activate or deactivate (e.g., \&quot;FT CB-2026\&quot;) | 
**document_kind** | **str** | Document kind the series belongs to. Required only when the same code backs series of more than one kind on the connection, which is legal. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.activate_series_request import ActivateSeriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateSeriesRequest from a JSON string
activate_series_request_instance = ActivateSeriesRequest.from_json(json)
# print the JSON string representation of the object
print(ActivateSeriesRequest.to_json())

# convert the object into a dict
activate_series_request_dict = activate_series_request_instance.to_dict()
# create an instance of ActivateSeriesRequest from a dict
activate_series_request_from_dict = ActivateSeriesRequest.from_dict(activate_series_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


