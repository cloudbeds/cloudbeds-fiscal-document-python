# CropLogoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crop_param** | [**CropParam**](CropParam.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.crop_logo_request import CropLogoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CropLogoRequest from a JSON string
crop_logo_request_instance = CropLogoRequest.from_json(json)
# print the JSON string representation of the object
print(CropLogoRequest.to_json())

# convert the object into a dict
crop_logo_request_dict = crop_logo_request_instance.to_dict()
# create an instance of CropLogoRequest from a dict
crop_logo_request_from_dict = CropLogoRequest.from_dict(crop_logo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


