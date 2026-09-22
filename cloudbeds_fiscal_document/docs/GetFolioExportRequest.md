# GetFolioExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folio_ids** | **List[int]** | Include transactions from the specified folio IDs. If omitted, all transactions for the source are included. The same filter set is applied to each selected folio. | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**source_id** | **int** | source ID of folio | 
**credit_debit_view** | **bool** | Should transactions be separated into debit/credits | [optional] 
**revenue_compact** | **bool** | Compact revenue transactions, valid only for sourceKind &#x3D; RESERVATION | [optional] 
**date_from** | **date** | Filter transactions with transaction datetime from this point (inclusive). Required for sourceKind &#x3D; HOUSE_ACCOUNT, optional for others. | [optional] 
**date_to** | **date** | Filter transactions with transaction datetime up to this point (inclusive). | [optional] 
**search_query** | **str** | Case-insensitive substring match on transaction description. | [optional] 
**description_filters** | **List[str]** | Composite identifiers used to filter by transaction type. Accepts the same values as POST /accounting/v1.0/folios/transactions descriptionFilters: typed item ids (\&quot;product_123\&quot;, \&quot;tax_456\&quot;, \&quot;addon_789\&quot;, \&quot;fee_101\&quot;, \&quot;custom_item_202\&quot;, \&quot;bookable_resource_303\&quot;), room revenue groups (\&quot;rate\&quot;, \&quot;roomRevenue_manual\&quot;, \&quot;roomRevenue_cancellation\&quot;, \&quot;roomRevenue_no_show\&quot;, \&quot;accountsReceivable\&quot;), or payment method codes (\&quot;cash\&quot;, \&quot;ebanking\&quot;, \&quot;cards_visa\&quot;, \&quot;cards_master\&quot;, \&quot;pay_pal\&quot;).  | [optional] 
**posted** | **bool** | Tri-state. true &#x3D; only posted, false &#x3D; only pending, omit &#x3D; both. | [optional] 
**include_voided** | **bool** | Include voided transactions and their full chain. Default true. | [optional] [default to True]
**sub_source_ids** | **List[int]** | Filter by sub-source IDs (booking room IDs for RESERVATION sources). Mirrors the same filter on POST /accounting/v1.0/folios/transactions.  | [optional] 
**sort** | [**List[FolioExportSort]**](FolioExportSort.md) | Optional ordering applied to the rendered transactions. Field names mirror POST /accounting/v1.0/folios/transactions: transaction_datetime, service_date, internal_code, description, notes, quantity, amount. When omitted the renderer uses its template default order.  | [optional] 
**format** | [**ExportFormat**](ExportFormat.md) |  | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.get_folio_export_request import GetFolioExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFolioExportRequest from a JSON string
get_folio_export_request_instance = GetFolioExportRequest.from_json(json)
# print the JSON string representation of the object
print(GetFolioExportRequest.to_json())

# convert the object into a dict
get_folio_export_request_dict = get_folio_export_request_instance.to_dict()
# create an instance of GetFolioExportRequest from a dict
get_folio_export_request_from_dict = GetFolioExportRequest.from_dict(get_folio_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


