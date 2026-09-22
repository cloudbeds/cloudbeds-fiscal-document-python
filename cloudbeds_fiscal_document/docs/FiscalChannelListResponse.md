# FiscalChannelListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[FiscalChannel]**](FiscalChannel.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.fiscal_channel_list_response import FiscalChannelListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalChannelListResponse from a JSON string
fiscal_channel_list_response_instance = FiscalChannelListResponse.from_json(json)
# print the JSON string representation of the object
print(FiscalChannelListResponse.to_json())

# convert the object into a dict
fiscal_channel_list_response_dict = fiscal_channel_list_response_instance.to_dict()
# create an instance of FiscalChannelListResponse from a dict
fiscal_channel_list_response_from_dict = FiscalChannelListResponse.from_dict(fiscal_channel_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


