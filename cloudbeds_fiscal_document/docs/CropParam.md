# CropParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | Left offset of the crop region in pixels | 
**y** | **int** | Top offset of the crop region in pixels | 
**width** | **int** | Width of the crop region in pixels | 
**height** | **int** | Height of the crop region in pixels | 

## Example

```python
from cloudbeds_fiscal_document.models.crop_param import CropParam

# TODO update the JSON string below
json = "{}"
# create an instance of CropParam from a JSON string
crop_param_instance = CropParam.from_json(json)
# print the JSON string representation of the object
print(CropParam.to_json())

# convert the object into a dict
crop_param_dict = crop_param_instance.to_dict()
# create an instance of CropParam from a dict
crop_param_from_dict = CropParam.from_dict(crop_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


