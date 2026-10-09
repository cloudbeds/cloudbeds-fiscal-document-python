# CreateInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | 
**transaction_id_to_amount** | **Dict[str, float]** | Map of transaction ID to amount (in major currency units, e.g., 10.50 for $10.50) for partial transaction inclusion | [optional] 
**transaction_id_to_display_amount** | **Dict[str, float]** | Map of transaction ID to amount in the invoice currency (major units, as in displayAmount) for partial transaction inclusion, recorded on the document exactly as given. Takes precedence over transactionIdToAmount for the same transaction. When the invoice currency is the property currency it behaves like transactionIdToAmount. | [optional] 
**source_id** | **int** |  | 
**sequence_id** | **int** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**user_id** | **int** |  | [optional] 
**currency** | **str** | Invoice currency. Selected transactions are converted into this currency at creation using the property&#39;s current exchange rate, which is locked on the issued document, and the converted amounts are fiscalized. Defaults to the property currency when omitted. | [optional] 
**recipient** | [**RecipientRequest**](RecipientRequest.md) |  | [optional] 
**manual_recipient** | [**ManualRecipientRequest**](ManualRecipientRequest.md) |  | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 
**simplified** | **bool** |  | [optional] [default to False]
**invoice_type** | **str** | Argentina RI only — the ARCA invoice class to issue (Factura A/B/T). Determines the ar-arca-doc-type sent to ARCA and the Punto de Venta series used. Ignored for non-RI / non-AR properties (those always issue C).  | [optional] 
**package_breakdown** | **bool** | Per-document override for package breakdown. Null means use property default. | [optional] 
**line_grouping_selection** | [**LineGroupingSelectionRequest**](LineGroupingSelectionRequest.md) |  | [optional] 
**due_date_property_timezone** | **date** |  | [optional] 
**note** | **str** |  | [optional] 
**emails** | **List[str]** | Optional list of email addresses to send the document to once it is ready | [optional] 
**subject** | **str** | Optional per-send override for the email subject. When omitted or blank, the subject is resolved from the property&#39;s email template, falling back to the service default. Supports the same [Placeholder] tokens as template subjects. | [optional] 
**summary** | **bool** | When true, marks this as a CFDI global/summary invoice (MX only) | [optional] [default to False]
**summary_frequency** | **str** | Reporting frequency for summary invoices (MX only) | [optional] 
**mx_cfdi_use** | **str** | MX only — SAT c_UsoCFDI code selected in the Create Invoice modal. Overrides the value stored in guest requirements (mx_cfdi_use). A generic RFC (XAXX/XEXX) always forces S01 at issuance time regardless of this value. | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.create_invoice_request import CreateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequest from a JSON string
create_invoice_request_instance = CreateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequest.to_json())

# convert the object into a dict
create_invoice_request_dict = create_invoice_request_instance.to_dict()
# create an instance of CreateInvoiceRequest from a dict
create_invoice_request_from_dict = CreateInvoiceRequest.from_dict(create_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


