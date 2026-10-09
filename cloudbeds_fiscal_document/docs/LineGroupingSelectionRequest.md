# LineGroupingSelectionRequest

Per-document grouping chosen in the create modal. Each omitted field keeps the property default. lineGrouping and posGrouping must be inside the property allowed set; otherwise the request is rejected. groupByRoom and groupByBusinessDate are free per-document modifiers: the property has no allowed set for them, only a default. Locked on the document once created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_grouping** | [**LineGrouping**](LineGrouping.md) |  | [optional] 
**pos_grouping** | [**PosGrouping**](PosGrouping.md) |  | [optional] 
**group_by_room** | **bool** |  | [optional] 
**group_by_business_date** | **bool** |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.line_grouping_selection_request import LineGroupingSelectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LineGroupingSelectionRequest from a JSON string
line_grouping_selection_request_instance = LineGroupingSelectionRequest.from_json(json)
# print the JSON string representation of the object
print(LineGroupingSelectionRequest.to_json())

# convert the object into a dict
line_grouping_selection_request_dict = line_grouping_selection_request_instance.to_dict()
# create an instance of LineGroupingSelectionRequest from a dict
line_grouping_selection_request_from_dict = LineGroupingSelectionRequest.from_dict(line_grouping_selection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


