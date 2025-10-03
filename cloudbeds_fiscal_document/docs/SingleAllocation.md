# SingleAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** |  | [optional] 
**allocated_amount** | **float** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.single_allocation import SingleAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of SingleAllocation from a JSON string
single_allocation_instance = SingleAllocation.from_json(json)
# print the JSON string representation of the object
print(SingleAllocation.to_json())

# convert the object into a dict
single_allocation_dict = single_allocation_instance.to_dict()
# create an instance of SingleAllocation from a dict
single_allocation_from_dict = SingleAllocation.from_dict(single_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


