# AllocationsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipt_id** | **int** |  | [optional] 
**source_id** | **int** |  | [optional] 
**source_identifier** | **str** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**allocations** | [**List[SingleAllocation]**](SingleAllocation.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.allocations_data import AllocationsData

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationsData from a JSON string
allocations_data_instance = AllocationsData.from_json(json)
# print the JSON string representation of the object
print(AllocationsData.to_json())

# convert the object into a dict
allocations_data_dict = allocations_data_instance.to_dict()
# create an instance of AllocationsData from a dict
allocations_data_from_dict = AllocationsData.from_dict(allocations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


