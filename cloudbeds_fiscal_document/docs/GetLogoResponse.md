# GetLogoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_url** | **str** | Presigned URL to access the logo file | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.get_logo_response import GetLogoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLogoResponse from a JSON string
get_logo_response_instance = GetLogoResponse.from_json(json)
# print the JSON string representation of the object
print(GetLogoResponse.to_json())

# convert the object into a dict
get_logo_response_dict = get_logo_response_instance.to_dict()
# create an instance of GetLogoResponse from a dict
get_logo_response_from_dict = GetLogoResponse.from_dict(get_logo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


