# AllocationsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **float** |  | [optional] 
**total_allocated** | **float** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.allocations_summary import AllocationsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationsSummary from a JSON string
allocations_summary_instance = AllocationsSummary.from_json(json)
# print the JSON string representation of the object
print(AllocationsSummary.to_json())

# convert the object into a dict
allocations_summary_dict = allocations_summary_instance.to_dict()
# create an instance of AllocationsSummary from a dict
allocations_summary_from_dict = AllocationsSummary.from_dict(allocations_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


