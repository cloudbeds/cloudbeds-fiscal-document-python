# LineGroupingSettings

New grouped line/POS rendering configuration. When absent on write the legacy boolean fields are used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_line_grouping** | [**LineGrouping**](LineGrouping.md) |  | 
**allowed_line_groupings** | [**List[LineGrouping]**](LineGrouping.md) |  | 
**default_pos_grouping** | [**PosGrouping**](PosGrouping.md) |  | 
**allowed_pos_groupings** | [**List[PosGrouping]**](PosGrouping.md) |  | 
**default_group_by_room** | **bool** |  | 
**default_group_by_business_date** | **bool** |  | 
**vat_display** | [**VatDisplay**](VatDisplay.md) |  | 

## Example

```python
from cloudbeds_fiscal_document.models.line_grouping_settings import LineGroupingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of LineGroupingSettings from a JSON string
line_grouping_settings_instance = LineGroupingSettings.from_json(json)
# print the JSON string representation of the object
print(LineGroupingSettings.to_json())

# convert the object into a dict
line_grouping_settings_dict = line_grouping_settings_instance.to_dict()
# create an instance of LineGroupingSettings from a dict
line_grouping_settings_from_dict = LineGroupingSettings.from_dict(line_grouping_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


