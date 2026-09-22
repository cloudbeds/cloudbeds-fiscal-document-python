# UpdateRequireAttentionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_attention** | **bool** | Whether the fiscal document requires attention. | 

## Example

```python
from cloudbeds_fiscal_document.models.update_require_attention_request import UpdateRequireAttentionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRequireAttentionRequest from a JSON string
update_require_attention_request_instance = UpdateRequireAttentionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRequireAttentionRequest.to_json())

# convert the object into a dict
update_require_attention_request_dict = update_require_attention_request_instance.to_dict()
# create an instance of UpdateRequireAttentionRequest from a dict
update_require_attention_request_from_dict = UpdateRequireAttentionRequest.from_dict(update_require_attention_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


