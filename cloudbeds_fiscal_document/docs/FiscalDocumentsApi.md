# cloudbeds_fiscal_document.FiscalDocumentsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_receipt_payment**](FiscalDocumentsApi.md#allocate_receipt_payment) | **POST** /fiscal-document/v1/fiscal-documents/receipt/allocate-payment | Allocate payment associated with receipt to charge transactions.
[**apply_receipt**](FiscalDocumentsApi.md#apply_receipt) | **POST** /fiscal-document/v1/fiscal-documents/receipts/{receiptId}/apply | Apply receipt to invoice
[**create_credit_note**](FiscalDocumentsApi.md#create_credit_note) | **POST** /fiscal-document/v1/fiscal-documents/credit-note | Create a fiscal document of the type credit note
[**create_invoice**](FiscalDocumentsApi.md#create_invoice) | **POST** /fiscal-document/v1/fiscal-documents/invoice | Create a fiscal document of the type invoice
[**create_pro_forma_invoice**](FiscalDocumentsApi.md#create_pro_forma_invoice) | **POST** /fiscal-document/v1/fiscal-documents/pro-forma-invoice | Create a fiscal document of the type pro forma invoice
[**create_receipt**](FiscalDocumentsApi.md#create_receipt) | **POST** /fiscal-document/v1/fiscal-documents/receipt | Create receipt for a payment.
[**create_rectify_invoice**](FiscalDocumentsApi.md#create_rectify_invoice) | **POST** /fiscal-document/v1/fiscal-documents/rectify-invoice | Create a fiscal document of the type rectify invoice
[**create_settlement_invoice**](FiscalDocumentsApi.md#create_settlement_invoice) | **POST** /fiscal-document/v1/fiscal-documents/{advance_invoice_id}/settlement | Create a settlement invoice for an advance invoice
[**create_simple_receipt**](FiscalDocumentsApi.md#create_simple_receipt) | **POST** /fiscal-document/v1/fiscal-documents/simple-receipt | Create simple receipts.
[**download_fiscal_document**](FiscalDocumentsApi.md#download_fiscal_document) | **GET** /fiscal-document/v1/fiscal-documents/{id}/download | Download fiscal document
[**email_fiscal_document**](FiscalDocumentsApi.md#email_fiscal_document) | **POST** /fiscal-document/v1/fiscal-documents/{id}/email | Email a fiscal document
[**get_allocations**](FiscalDocumentsApi.md#get_allocations) | **GET** /fiscal-document/v1/fiscal-documents/allocations | Get payment allocation transactions
[**get_allocations_summary**](FiscalDocumentsApi.md#get_allocations_summary) | **GET** /fiscal-document/v1/fiscal-documents/allocations/summary | Get allocations summary
[**get_count_fiscal_documents_with_discrepancies**](FiscalDocumentsApi.md#get_count_fiscal_documents_with_discrepancies) | **GET** /fiscal-document/v1/fiscal-documents/discrepancies/summary | Get count of fiscal documents with discrepancies
[**get_credit_note_preview**](FiscalDocumentsApi.md#get_credit_note_preview) | **POST** /fiscal-document/v1/fiscal-documents/credit-note/preview | Get fiscal document preview of the type credit note
[**get_document_preview**](FiscalDocumentsApi.md#get_document_preview) | **POST** /fiscal-document/v1/fiscal-documents/invoice/preview | Get fiscal document preview of the type invoice
[**get_document_rules**](FiscalDocumentsApi.md#get_document_rules) | **GET** /fiscal-document/v1/fiscal-documents/rules | Get document creation rules for a given document kind
[**get_fiscal_document_email_subject**](FiscalDocumentsApi.md#get_fiscal_document_email_subject) | **GET** /fiscal-document/v1/fiscal-documents/email-subject | Resolve the email subject for a fiscal document
[**get_fiscal_document_recipients_by_id**](FiscalDocumentsApi.md#get_fiscal_document_recipients_by_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/recipients | Get list of recipients associated to the fiscal document
[**get_fiscal_document_transactions**](FiscalDocumentsApi.md#get_fiscal_document_transactions) | **GET** /fiscal-document/v1/fiscal-documents/transactions | Get available transactions for fiscal documents
[**get_fiscal_document_transactions_by_id**](FiscalDocumentsApi.md#get_fiscal_document_transactions_by_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/transactions | Get list of transactions for a given fiscal document id
[**get_fiscal_document_transactions_for_allocation**](FiscalDocumentsApi.md#get_fiscal_document_transactions_for_allocation) | **GET** /fiscal-document/v1/fiscal-documents/allocations/transactions | Get available transactions for allocations
[**get_fiscal_documents**](FiscalDocumentsApi.md#get_fiscal_documents) | **GET** /fiscal-document/v1/fiscal-documents | Get list of fiscal documents
[**get_invoice_allocations**](FiscalDocumentsApi.md#get_invoice_allocations) | **GET** /fiscal-document/v1/invoices/{id}/receipts/allocations | Get allocations for an invoice
[**get_pro_forma_preview**](FiscalDocumentsApi.md#get_pro_forma_preview) | **POST** /fiscal-document/v1/fiscal-documents/pro-forma-invoice/preview | Create a fiscal document of the type pro forma invoice
[**get_rectify_invoice_preview**](FiscalDocumentsApi.md#get_rectify_invoice_preview) | **POST** /fiscal-document/v1/fiscal-documents/rectify-invoice/preview | Get fiscal document preview of the type rectify invoice
[**get_selected_transactions_summary**](FiscalDocumentsApi.md#get_selected_transactions_summary) | **GET** /fiscal-document/v1/fiscal-documents/transactions/summary | Get totals of selected available transactions for fiscal documents (deprecated)
[**get_transactions_summary_by_document_id**](FiscalDocumentsApi.md#get_transactions_summary_by_document_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/transactions/summary | Get totals of transactions for a given fiscal document id
[**post_selected_transactions_summary**](FiscalDocumentsApi.md#post_selected_transactions_summary) | **POST** /fiscal-document/v1/fiscal-documents/transactions/summary | Get totals of selected available transactions for fiscal documents
[**put_fiscal_document**](FiscalDocumentsApi.md#put_fiscal_document) | **PUT** /fiscal-document/v1/fiscal-documents/{id} | Update a fiscal document by id
[**update_pro_forma_invoice_status**](FiscalDocumentsApi.md#update_pro_forma_invoice_status) | **PUT** /fiscal-document/v1/fiscal-documents/pro-forma-invoice/{id}/status | Update pro forma invoice status
[**update_require_attention**](FiscalDocumentsApi.md#update_require_attention) | **PATCH** /fiscal-document/v1/fiscal-documents/{id}/require-attention | Update require attention flag for a fiscal document
[**void_receipt**](FiscalDocumentsApi.md#void_receipt) | **POST** /fiscal-document/v1/fiscal-documents/receipts/{receiptId}/void | Void a receipt


# **allocate_receipt_payment**
> FiscalDocumentSummaryResponse allocate_receipt_payment(x_property_id, allocate_receipt_payment_request)

Allocate payment associated with receipt to charge transactions.

Allocate payment associated with receipt to charge transactions.
The amounts of all allocations must be equal to the payment amount.
The transactions should not be fully allocated already
  and the amount allocated should not be more than the remaining balance on the transaction.
All transactions not part of an invoice will be added to newly created invoice.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.allocate_receipt_payment_request import AllocateReceiptPaymentRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    allocate_receipt_payment_request = cloudbeds_fiscal_document.AllocateReceiptPaymentRequest() # AllocateReceiptPaymentRequest | 

    try:
        # Allocate payment associated with receipt to charge transactions.
        api_response = api_instance.allocate_receipt_payment(x_property_id, allocate_receipt_payment_request)
        print("The response of FiscalDocumentsApi->allocate_receipt_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->allocate_receipt_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **allocate_receipt_payment_request** | [**AllocateReceiptPaymentRequest**](AllocateReceiptPaymentRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Receipt will be accepted to start the process of document creation according to country rules |  -  |
**400** | Bad Request |  -  |
**404** | Payment or payment transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_receipt**
> apply_receipt(x_property_id, receipt_id, apply_receipt_request)

Apply receipt to invoice

Apply receipt to invoice. Receipt should not have allocations


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.apply_receipt_request import ApplyReceiptRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    receipt_id = 56 # int | The ID of the receipt
    apply_receipt_request = cloudbeds_fiscal_document.ApplyReceiptRequest() # ApplyReceiptRequest | 

    try:
        # Apply receipt to invoice
        api_instance.apply_receipt(x_property_id, receipt_id, apply_receipt_request)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->apply_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **receipt_id** | **int**| The ID of the receipt | 
 **apply_receipt_request** | [**ApplyReceiptRequest**](ApplyReceiptRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Receipt successfully voided |  -  |
**400** | Bad Request - Invalid status or document type |  -  |
**404** | Receipt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note**
> FiscalDocumentSummaryResponse create_credit_note(x_property_id, create_credit_note_request)

Create a fiscal document of the type credit note

Create a fiscal document of the type credit note.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_credit_note_request import CreateCreditNoteRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    create_credit_note_request = cloudbeds_fiscal_document.CreateCreditNoteRequest() # CreateCreditNoteRequest | 

    try:
        # Create a fiscal document of the type credit note
        api_response = api_instance.create_credit_note(x_property_id, create_credit_note_request)
        print("The response of FiscalDocumentsApi->create_credit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_credit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **create_credit_note_request** | [**CreateCreditNoteRequest**](CreateCreditNoteRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | The source&#39;s transactions are being reconciled, or pending transaction discrepancies were found. The credit note was not created — retry the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice**
> FiscalDocumentSummaryResponse create_invoice(x_property_id, create_invoice_request)

Create a fiscal document of the type invoice

Create a fiscal document of the type invoice.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_invoice_request import CreateInvoiceRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    create_invoice_request = cloudbeds_fiscal_document.CreateInvoiceRequest() # CreateInvoiceRequest | 

    try:
        # Create a fiscal document of the type invoice
        api_response = api_instance.create_invoice(x_property_id, create_invoice_request)
        print("The response of FiscalDocumentsApi->create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **create_invoice_request** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pro_forma_invoice**
> FiscalDocumentSummaryResponse create_pro_forma_invoice(x_property_id, pro_forma_invoice_request)

Create a fiscal document of the type pro forma invoice

Create a fiscal document of the type pro forma invoice.

**Pro Forma Invoice Characteristics:**
- Contains pending transactions that are subject to change
- Includes payment information
- Transactions are NOT locked (unlike regular invoices)
- Can be converted to regular invoices later when transactions are posted
- Has its own sequence numbering and settings


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.pro_forma_invoice_request import ProFormaInvoiceRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    pro_forma_invoice_request = cloudbeds_fiscal_document.ProFormaInvoiceRequest() # ProFormaInvoiceRequest | 

    try:
        # Create a fiscal document of the type pro forma invoice
        api_response = api_instance.create_pro_forma_invoice(x_property_id, pro_forma_invoice_request)
        print("The response of FiscalDocumentsApi->create_pro_forma_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_pro_forma_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **pro_forma_invoice_request** | [**ProFormaInvoiceRequest**](ProFormaInvoiceRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt**
> FiscalDocumentSummaryResponse create_receipt(x_property_id, create_receipt_request)

Create receipt for a payment.

Create a receipt for a payment and optionally specify allocations per transaction.
In case of no allocations, a 'Simple receipt' will be created that can later be allocated to charge transactions.
The amounts of all allocations must be equal to the payment amount.
The transactions should not be fully allocated already
  and the amount allocated should not be more than the remaining balance on the transaction.
All transactions not part of an invoice will be added to newly created invoice.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_receipt_request import CreateReceiptRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    create_receipt_request = cloudbeds_fiscal_document.CreateReceiptRequest() # CreateReceiptRequest | 

    try:
        # Create receipt for a payment.
        api_response = api_instance.create_receipt(x_property_id, create_receipt_request)
        print("The response of FiscalDocumentsApi->create_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **create_receipt_request** | [**CreateReceiptRequest**](CreateReceiptRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Receipt successfully created |  -  |
**400** | Bad Request |  -  |
**404** | Payment or payment transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rectify_invoice**
> FiscalDocumentSummaryResponse create_rectify_invoice(x_property_id, rectify_invoice_note_request)

Create a fiscal document of the type rectify invoice

Create a fiscal document of the type rectify invoice.

**Spanish Fiscal Regulations:**
- Only available for properties in Spain
- An invoice that has already been rectified cannot be rectified again
- To make corrections to a rectified invoice, you must rectify the most recent invoice in the rectification chain

**Validation Rules:**
- The target invoice must not have been previously rectified
- If the invoice has been rectified, the API will return an error with details about which invoice should be rectified instead


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.rectify_invoice_note_request import RectifyInvoiceNoteRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    rectify_invoice_note_request = cloudbeds_fiscal_document.RectifyInvoiceNoteRequest() # RectifyInvoiceNoteRequest | 

    try:
        # Create a fiscal document of the type rectify invoice
        api_response = api_instance.create_rectify_invoice(x_property_id, rectify_invoice_note_request)
        print("The response of FiscalDocumentsApi->create_rectify_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_rectify_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **rectify_invoice_note_request** | [**RectifyInvoiceNoteRequest**](RectifyInvoiceNoteRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Validation errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settlement_invoice**
> FiscalDocumentSummaryResponse create_settlement_invoice(x_property_id, advance_invoice_id, create_settlement_invoice_request)

Create a settlement invoice for an advance invoice

Create a settlement invoice linked to an existing advance invoice.

A settlement invoice finalizes the billing cycle started by an advance invoice.
It references the advance invoice and may include additional transactions
that were not part of the original advance.

**Validation Rules:**
- The parent document must be an ADVANCE_INVOICE
- The parent document must be in an active status
- There must not already be an active settlement invoice for this advance


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_settlement_invoice_request import CreateSettlementInvoiceRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    advance_invoice_id = 56 # int | The ID of the advance invoice to settle
    create_settlement_invoice_request = cloudbeds_fiscal_document.CreateSettlementInvoiceRequest() # CreateSettlementInvoiceRequest | 

    try:
        # Create a settlement invoice for an advance invoice
        api_response = api_instance.create_settlement_invoice(x_property_id, advance_invoice_id, create_settlement_invoice_request)
        print("The response of FiscalDocumentsApi->create_settlement_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_settlement_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **advance_invoice_id** | **int**| The ID of the advance invoice to settle | 
 **create_settlement_invoice_request** | [**CreateSettlementInvoiceRequest**](CreateSettlementInvoiceRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_simple_receipt**
> List[FiscalDocumentSummaryResponse] create_simple_receipt(x_property_id, create_simple_receipt_request)

Create simple receipts.

Create receipts for list of payments without allocations.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_simple_receipt_request import CreateSimpleReceiptRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    create_simple_receipt_request = cloudbeds_fiscal_document.CreateSimpleReceiptRequest() # CreateSimpleReceiptRequest | 

    try:
        # Create simple receipts.
        api_response = api_instance.create_simple_receipt(x_property_id, create_simple_receipt_request)
        print("The response of FiscalDocumentsApi->create_simple_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->create_simple_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **create_simple_receipt_request** | [**CreateSimpleReceiptRequest**](CreateSimpleReceiptRequest.md)|  | 

### Return type

[**List[FiscalDocumentSummaryResponse]**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Receipt successfully created |  -  |
**400** | Bad Request |  -  |
**404** | Payment or payment transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_fiscal_document**
> bytearray download_fiscal_document(id, x_property_id, file_id=file_id)

Download fiscal document

Initiates the download of the fiscal document file. When fileId is provided, downloads that stored file instead (see files on the list response); an absent or blank fileId downloads the primary file.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 'id_example' # str | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id
    file_id = 'file_id_example' # str |  (optional)

    try:
        # Download fiscal document
        api_response = api_instance.download_fiscal_document(id, x_property_id, file_id=file_id)
        print("The response of FiscalDocumentsApi->download_fiscal_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->download_fiscal_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 
 **file_id** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |
**404** | Document or file not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_fiscal_document**
> object email_fiscal_document(id, x_property_id, fiscal_document_email_request)

Email a fiscal document

Initiates the process to send the invoice to a customer

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_email_request import FiscalDocumentEmailRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 'id_example' # str | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id
    fiscal_document_email_request = cloudbeds_fiscal_document.FiscalDocumentEmailRequest() # FiscalDocumentEmailRequest | 

    try:
        # Email a fiscal document
        api_response = api_instance.email_fiscal_document(id, x_property_id, fiscal_document_email_request)
        print("The response of FiscalDocumentsApi->email_fiscal_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->email_fiscal_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 
 **fiscal_document_email_request** | [**FiscalDocumentEmailRequest**](FiscalDocumentEmailRequest.md)|  | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocations**
> List[AllocationsData] get_allocations(x_property_id, source_ids=source_ids, source_identifiers=source_identifiers, source_kind=source_kind, receipt_ids=receipt_ids)

Get payment allocation transactions

Retrieves payment allocations.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.allocations_data import AllocationsData
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    source_ids = [56] # List[int] | source IDs. (optional)
    source_identifiers = ['source_identifiers_example'] # List[str] | source Identifiers. (optional)
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind. (optional)
    receipt_ids = [56] # List[int] | document IDs. (optional)

    try:
        # Get payment allocation transactions
        api_response = api_instance.get_allocations(x_property_id, source_ids=source_ids, source_identifiers=source_identifiers, source_kind=source_kind, receipt_ids=receipt_ids)
        print("The response of FiscalDocumentsApi->get_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_ids** | [**List[int]**](int.md)| source IDs. | [optional] 
 **source_identifiers** | [**List[str]**](str.md)| source Identifiers. | [optional] 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | [optional] 
 **receipt_ids** | [**List[int]**](int.md)| document IDs. | [optional] 

### Return type

[**List[AllocationsData]**](AllocationsData.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocations_summary**
> AllocationsSummary get_allocations_summary(x_property_id, source_id, source_kind, folio_ids=folio_ids, document_ids=document_ids)

Get allocations summary

Retrieves allocations summary.


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.allocations_summary import AllocationsSummary
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    source_id = 56 # int | source ID.
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind.
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)
    document_ids = [56] # List[int] | document IDs. (optional)

    try:
        # Get allocations summary
        api_response = api_instance.get_allocations_summary(x_property_id, source_id, source_kind, folio_ids=folio_ids, document_ids=document_ids)
        print("The response of FiscalDocumentsApi->get_allocations_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_allocations_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_id** | **int**| source ID. | 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | 
 **folio_ids** | [**List[int]**](int.md)| Filter by folio IDs. | [optional] 
 **document_ids** | [**List[int]**](int.md)| document IDs. | [optional] 

### Return type

[**AllocationsSummary**](AllocationsSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_fiscal_documents_with_discrepancies**
> DiscrepanciesCount get_count_fiscal_documents_with_discrepancies(x_property_id, source_id, source_kind)

Get count of fiscal documents with discrepancies

Returns the count of fiscal documents that have discrepancies, filtered by sourceId and sourceKind.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.discrepancies_count import DiscrepanciesCount
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    source_id = 'source_id_example' # str | Source ID to filter documents by.
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Source kind to filter documents by.

    try:
        # Get count of fiscal documents with discrepancies
        api_response = api_instance.get_count_fiscal_documents_with_discrepancies(x_property_id, source_id, source_kind)
        print("The response of FiscalDocumentsApi->get_count_fiscal_documents_with_discrepancies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_count_fiscal_documents_with_discrepancies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_id** | **str**| Source ID to filter documents by. | 
 **source_kind** | [**SourceKind**](.md)| Source kind to filter documents by. | 

### Return type

[**DiscrepanciesCount**](DiscrepanciesCount.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_preview**
> bytearray get_credit_note_preview(x_property_id, get_credit_note_preview_request)

Get fiscal document preview of the type credit note

Get fiscal document preview of the type credit note.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_credit_note_preview_request import GetCreditNotePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    get_credit_note_preview_request = cloudbeds_fiscal_document.GetCreditNotePreviewRequest() # GetCreditNotePreviewRequest | 

    try:
        # Get fiscal document preview of the type credit note
        api_response = api_instance.get_credit_note_preview(x_property_id, get_credit_note_preview_request)
        print("The response of FiscalDocumentsApi->get_credit_note_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_credit_note_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **get_credit_note_preview_request** | [**GetCreditNotePreviewRequest**](GetCreditNotePreviewRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_preview**
> bytearray get_document_preview(x_property_id, get_invoice_preview_request)

Get fiscal document preview of the type invoice

Get fiscal document preview of the type invoice.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_invoice_preview_request import GetInvoicePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    get_invoice_preview_request = cloudbeds_fiscal_document.GetInvoicePreviewRequest() # GetInvoicePreviewRequest | 

    try:
        # Get fiscal document preview of the type invoice
        api_response = api_instance.get_document_preview(x_property_id, get_invoice_preview_request)
        print("The response of FiscalDocumentsApi->get_document_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_document_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **get_invoice_preview_request** | [**GetInvoicePreviewRequest**](GetInvoicePreviewRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_rules**
> List[FieldDefinition] get_document_rules(x_property_id, document_kind, accept_language=accept_language)

Get document creation rules for a given document kind

Returns field definitions that the UI must collect when creating a document of the given kind.
Uses the same FieldDefinition schema as action.fields on document actions.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.field_definition import FieldDefinition
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | 
    accept_language = 'accept_language_example' # str | Desired language of exported PDF (optional)

    try:
        # Get document creation rules for a given document kind
        api_response = api_instance.get_document_rules(x_property_id, document_kind, accept_language=accept_language)
        print("The response of FiscalDocumentsApi->get_document_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_document_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **document_kind** | [**FiscalDocumentKind**](.md)|  | 
 **accept_language** | **str**| Desired language of exported PDF | [optional] 

### Return type

[**List[FieldDefinition]**](FieldDefinition.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of field definitions for document creation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_document_email_subject**
> EmailSubjectResponse get_fiscal_document_email_subject(x_property_id, document_id=document_id, document_kind=document_kind, source_kind=source_kind, source_id=source_id, recipient_type=recipient_type, recipient_id=recipient_id)

Resolve the email subject for a fiscal document

Returns the subject the service would put on the email, so a UI can seed an editable Subject
field from the same resolution the send uses rather than reimplementing it.

Give `documentId` for a document that exists. The answer is then exactly what a send with no
subject override produces: a token the service holds no value for resolves to an empty
string, as it would in the delivered email.

Give `documentKind`, `sourceKind` and `sourceId` instead for a document about to be created.
A token whose value is only assigned at creation is then returned **verbatim**, for example
`Grand Hotel - Invoice #[Invoice Number]`. Send the string back, edited or not, on the create
request and the service fills those tokens in once the values exist.

Supplying the chosen recipient lets the guest's language win when the property has
"use guest language" enabled; without it the subject falls back to the property's language.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.email_subject_recipient_type import EmailSubjectRecipientType
from cloudbeds_fiscal_document.models.email_subject_response import EmailSubjectResponse
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    document_id = 'document_id_example' # str | An existing fiscal document. When given, the document parameters below are ignored - everything is derived from the document itself.  (optional)
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Required when documentId is absent. (optional)
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Required when documentId is absent. (optional)
    source_id = 56 # int | Required when documentId is absent. (optional)
    recipient_type = cloudbeds_fiscal_document.EmailSubjectRecipientType() # EmailSubjectRecipientType | The chosen Bill-to recipient. Supply together with recipientId. Optional because a manually entered recipient has no stored record to point at; the subject then resolves in the property's language rather than the guest's.  (optional)
    recipient_id = 56 # int | The chosen Bill-to recipient. Supply together with recipientType. (optional)

    try:
        # Resolve the email subject for a fiscal document
        api_response = api_instance.get_fiscal_document_email_subject(x_property_id, document_id=document_id, document_kind=document_kind, source_kind=source_kind, source_id=source_id, recipient_type=recipient_type, recipient_id=recipient_id)
        print("The response of FiscalDocumentsApi->get_fiscal_document_email_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_document_email_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **document_id** | **str**| An existing fiscal document. When given, the document parameters below are ignored - everything is derived from the document itself.  | [optional] 
 **document_kind** | [**FiscalDocumentKind**](.md)| Required when documentId is absent. | [optional] 
 **source_kind** | [**SourceKind**](.md)| Required when documentId is absent. | [optional] 
 **source_id** | **int**| Required when documentId is absent. | [optional] 
 **recipient_type** | [**EmailSubjectRecipientType**](.md)| The chosen Bill-to recipient. Supply together with recipientId. Optional because a manually entered recipient has no stored record to point at; the subject then resolves in the property&#39;s language rather than the guest&#39;s.  | [optional] 
 **recipient_id** | **int**| The chosen Bill-to recipient. Supply together with recipientType. | [optional] 

### Return type

[**EmailSubjectResponse**](EmailSubjectResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_document_recipients_by_id**
> List[FiscalDocumentRecipient] get_fiscal_document_recipients_by_id(id, x_property_id)

Get list of recipients associated to the fiscal document

Retrieves a list of recipients associated to the transaction.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_recipient import FiscalDocumentRecipient
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 'id_example' # str | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id

    try:
        # Get list of recipients associated to the fiscal document
        api_response = api_instance.get_fiscal_document_recipients_by_id(id, x_property_id)
        print("The response of FiscalDocumentsApi->get_fiscal_document_recipients_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_document_recipients_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 

### Return type

[**List[FiscalDocumentRecipient]**](FiscalDocumentRecipient.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_document_transactions**
> FiscalDocumentTransactionsPaginated get_fiscal_document_transactions(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids, nest_taxes=nest_taxes, show_invoiced=show_invoiced, currency=currency)

Get available transactions for fiscal documents

Retrieves a paginated list of available transactions for a source based on the document type.
- For INVOICE: Returns posted (paid) transactions, and pending transactions when feature.fiscal-document.pending-transactions is enabled
- For CREDIT_NOTE: Returns posted (paid) transactions, and pending transactions when feature.fiscal-document.pending-transactions is enabled
- For PRO_FORMA_INVOICE: Returns both pending transactions and posted (paid) payments
- Transactions already included in fiscal documents are excluded unless show_invoiced=true
- Each transaction includes a status field (PENDING or POSTED)


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.models.fiscal_document_transactions_paginated import FiscalDocumentTransactionsPaginated
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    source_id = 56 # int | source ID.
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind.
    for_document_type = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related (deprecated, use `documentKind` instead). (optional)
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related. (optional)
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    sort = 'createdAt:desc' # str | Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode (optional)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)
    nest_taxes = False # bool | When true, VAT tax transactions are nested inside their parent transaction's taxes field and removed from the top-level list. Only taxes whose configuration is classified as VAT are nested; everything else (city and municipal taxes, fees, custom item taxes not classified as VAT) stays in the top-level list with no link back to its parent, so the parent-child relationship for those has to be read from the same endpoint called without nestTaxes. A VAT tax is only ever returned together with its parent transaction: where the parent is not in the response, the tax is omitted entirely rather than returned at the top level. (optional) (default to False)
    show_invoiced = False # bool | When true, transactions already included in fiscal documents are not filtered out. (optional) (default to False)
    currency = 'currency_example' # str | Invoice currency to convert every transaction into. Each transaction's amount is converted to this currency using the property's current exchange rate and returned in the display* fields; the original amount and currency are also returned. When omitted, no conversion is applied. (optional)

    try:
        # Get available transactions for fiscal documents
        api_response = api_instance.get_fiscal_document_transactions(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids, nest_taxes=nest_taxes, show_invoiced=show_invoiced, currency=currency)
        print("The response of FiscalDocumentsApi->get_fiscal_document_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_document_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_id** | **int**| source ID. | 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | 
 **for_document_type** | [**FiscalDocumentKind**](.md)| Document type for which transactions are related (deprecated, use &#x60;documentKind&#x60; instead). | [optional] 
 **document_kind** | [**FiscalDocumentKind**](.md)| Document type for which transactions are related. | [optional] 
 **page_token** | **str**| Token for fetching the next page, as per cursor-based pagination. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **sort** | **str**| Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode | [optional] 
 **folio_ids** | [**List[int]**](int.md)| Filter by folio IDs. | [optional] 
 **nest_taxes** | **bool**| When true, VAT tax transactions are nested inside their parent transaction&#39;s taxes field and removed from the top-level list. Only taxes whose configuration is classified as VAT are nested; everything else (city and municipal taxes, fees, custom item taxes not classified as VAT) stays in the top-level list with no link back to its parent, so the parent-child relationship for those has to be read from the same endpoint called without nestTaxes. A VAT tax is only ever returned together with its parent transaction: where the parent is not in the response, the tax is omitted entirely rather than returned at the top level. | [optional] [default to False]
 **show_invoiced** | **bool**| When true, transactions already included in fiscal documents are not filtered out. | [optional] [default to False]
 **currency** | **str**| Invoice currency to convert every transaction into. Each transaction&#39;s amount is converted to this currency using the property&#39;s current exchange rate and returned in the display* fields; the original amount and currency are also returned. When omitted, no conversion is applied. | [optional] 

### Return type

[**FiscalDocumentTransactionsPaginated**](FiscalDocumentTransactionsPaginated.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | The source&#39;s transactions are being reconciled, or pending transaction discrepancies were found. The list is not safe to act on yet — retry the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_document_transactions_by_id**
> FiscalDocumentTransactionsPaginated get_fiscal_document_transactions_by_id(id, x_property_id, page_token=page_token, include_linked_document_transactions=include_linked_document_transactions, sort=sort, limit=limit, folio_ids=folio_ids, nest_taxes=nest_taxes, currency=currency)

Get list of transactions for a given fiscal document id

Retrieves a paginated list of available transactions for fiscal document id.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_paginated import FiscalDocumentTransactionsPaginated
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 'id_example' # str | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    include_linked_document_transactions = False # bool | Include transactions from linked documents. (optional) (default to False)
    sort = 'createdAt:desc' # str | Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)
    nest_taxes = False # bool | When true, VAT tax transactions are nested inside their parent transaction's taxes field and removed from the top-level list. Only taxes whose configuration is classified as VAT are nested; everything else (city and municipal taxes, fees, custom item taxes not classified as VAT) stays in the top-level list with no link back to its parent, so the parent-child relationship for those has to be read from the same endpoint called without nestTaxes. A VAT tax is only ever returned together with its parent transaction: where the parent is not part of the document, the tax is omitted from the response entirely rather than returned at the top level. (optional) (default to False)
    currency = 'currency_example' # str | Invoice currency to convert every transaction into. Each transaction's amount is converted to this currency using the property's current exchange rate and returned in the display* fields; the original amount and currency are also returned. When omitted, no conversion is applied. (optional)

    try:
        # Get list of transactions for a given fiscal document id
        api_response = api_instance.get_fiscal_document_transactions_by_id(id, x_property_id, page_token=page_token, include_linked_document_transactions=include_linked_document_transactions, sort=sort, limit=limit, folio_ids=folio_ids, nest_taxes=nest_taxes, currency=currency)
        print("The response of FiscalDocumentsApi->get_fiscal_document_transactions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_document_transactions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 
 **page_token** | **str**| Token for fetching the next page, as per cursor-based pagination. | [optional] 
 **include_linked_document_transactions** | **bool**| Include transactions from linked documents. | [optional] [default to False]
 **sort** | **str**| Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **folio_ids** | [**List[int]**](int.md)| Filter by folio IDs. | [optional] 
 **nest_taxes** | **bool**| When true, VAT tax transactions are nested inside their parent transaction&#39;s taxes field and removed from the top-level list. Only taxes whose configuration is classified as VAT are nested; everything else (city and municipal taxes, fees, custom item taxes not classified as VAT) stays in the top-level list with no link back to its parent, so the parent-child relationship for those has to be read from the same endpoint called without nestTaxes. A VAT tax is only ever returned together with its parent transaction: where the parent is not part of the document, the tax is omitted from the response entirely rather than returned at the top level. | [optional] [default to False]
 **currency** | **str**| Invoice currency to convert every transaction into. Each transaction&#39;s amount is converted to this currency using the property&#39;s current exchange rate and returned in the display* fields; the original amount and currency are also returned. When omitted, no conversion is applied. | [optional] 

### Return type

[**FiscalDocumentTransactionsPaginated**](FiscalDocumentTransactionsPaginated.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_document_transactions_for_allocation**
> FiscalDocumentTransactionsForAllocationPaginated get_fiscal_document_transactions_for_allocation(x_property_id, source_id, source_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids, document_ids=document_ids, document_id=document_id, statuses=statuses)

Get available transactions for allocations

Retrieves a paginated list of available transactions for allocations.


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_for_allocation_paginated import FiscalDocumentTransactionsForAllocationPaginated
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.models.transaction_status import TransactionStatus
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    source_id = 56 # int | source ID.
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind.
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    sort = 'createdAt:desc' # str | Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode (optional)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)
    document_ids = [56] # List[int] | document IDs. (optional)
    document_id = 56 # int | document ID. (optional)
    statuses = [cloudbeds_fiscal_document.TransactionStatus()] # List[TransactionStatus] | Filter by status. (optional)

    try:
        # Get available transactions for allocations
        api_response = api_instance.get_fiscal_document_transactions_for_allocation(x_property_id, source_id, source_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids, document_ids=document_ids, document_id=document_id, statuses=statuses)
        print("The response of FiscalDocumentsApi->get_fiscal_document_transactions_for_allocation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_document_transactions_for_allocation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_id** | **int**| source ID. | 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | 
 **page_token** | **str**| Token for fetching the next page, as per cursor-based pagination. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **sort** | **str**| Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode | [optional] 
 **folio_ids** | [**List[int]**](int.md)| Filter by folio IDs. | [optional] 
 **document_ids** | [**List[int]**](int.md)| document IDs. | [optional] 
 **document_id** | **int**| document ID. | [optional] 
 **statuses** | [**List[TransactionStatus]**](TransactionStatus.md)| Filter by status. | [optional] 

### Return type

[**FiscalDocumentTransactionsForAllocationPaginated**](FiscalDocumentTransactionsForAllocationPaginated.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_documents**
> FiscalDocumentPaginated get_fiscal_documents(x_property_id, page_token=page_token, sort=sort, limit=limit, filters=filters)

Get list of fiscal documents

Retrieves a paginated list of fiscal documents filtered by optional criteria.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_filters import FiscalDocumentFilters
from cloudbeds_fiscal_document.models.fiscal_document_paginated import FiscalDocumentPaginated
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    sort = 'createdAt:desc' # str | Supported fields:  - createdAt  - dueDate  - invoiceDate  - kind  - status  Supported sort modes asc:desc. If not supplied default is asc.  (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    filters = cloudbeds_fiscal_document.FiscalDocumentFilters() # FiscalDocumentFilters |  (optional)

    try:
        # Get list of fiscal documents
        api_response = api_instance.get_fiscal_documents(x_property_id, page_token=page_token, sort=sort, limit=limit, filters=filters)
        print("The response of FiscalDocumentsApi->get_fiscal_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **page_token** | **str**| Token for fetching the next page, as per cursor-based pagination. | [optional] 
 **sort** | **str**| Supported fields:  - createdAt  - dueDate  - invoiceDate  - kind  - status  Supported sort modes asc:desc. If not supplied default is asc.  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **filters** | [**FiscalDocumentFilters**](.md)|  | [optional] 

### Return type

[**FiscalDocumentPaginated**](FiscalDocumentPaginated.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_allocations**
> InvoiceAllocationsResponse get_invoice_allocations(x_property_id, id)

Get allocations for an invoice

Retrieves all active allocations for the specified invoice, grouped by transaction ID.
Only includes allocations from receipts with active statuses.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.invoice_allocations_response import InvoiceAllocationsResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    id = 'id_example' # str | Invoice ID

    try:
        # Get allocations for an invoice
        api_response = api_instance.get_invoice_allocations(x_property_id, id)
        print("The response of FiscalDocumentsApi->get_invoice_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_invoice_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **id** | **str**| Invoice ID | 

### Return type

[**InvoiceAllocationsResponse**](InvoiceAllocationsResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Invalid request (document is not an invoice or invalid ID format) |  -  |
**404** | Bad Request - Invoice not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pro_forma_preview**
> bytearray get_pro_forma_preview(x_property_id, pro_forma_invoice_preview_request)

Create a fiscal document of the type pro forma invoice

Create a fiscal document of the type pro forma invoice.

**Pro Forma Invoice Characteristics:**
- Contains pending transactions that are subject to change
- Includes payment information
- Transactions are NOT locked (unlike regular invoices)
- Can be converted to regular invoices later when transactions are posted
- Has its own sequence numbering and settings


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.pro_forma_invoice_preview_request import ProFormaInvoicePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    pro_forma_invoice_preview_request = cloudbeds_fiscal_document.ProFormaInvoicePreviewRequest() # ProFormaInvoicePreviewRequest | 

    try:
        # Create a fiscal document of the type pro forma invoice
        api_response = api_instance.get_pro_forma_preview(x_property_id, pro_forma_invoice_preview_request)
        print("The response of FiscalDocumentsApi->get_pro_forma_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_pro_forma_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **pro_forma_invoice_preview_request** | [**ProFormaInvoicePreviewRequest**](ProFormaInvoicePreviewRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rectify_invoice_preview**
> bytearray get_rectify_invoice_preview(x_property_id, get_rectify_invoice_note_preview_request)

Get fiscal document preview of the type rectify invoice

Get fiscal document preview of the type rectify invoice.
**Spanish Fiscal Regulations:**
- Only available for properties in Spain
- An invoice that has already been rectified cannot be rectified again
- To make corrections to a rectified invoice, you must rectify the most recent invoice in the rectification chain
**Validation Rules:**
- The target invoice must not have been previously rectified
- If the invoice has been rectified, the API will return an error with details about which invoice should be rectified instead


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_rectify_invoice_note_preview_request import GetRectifyInvoiceNotePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    get_rectify_invoice_note_preview_request = cloudbeds_fiscal_document.GetRectifyInvoiceNotePreviewRequest() # GetRectifyInvoiceNotePreviewRequest | 

    try:
        # Get fiscal document preview of the type rectify invoice
        api_response = api_instance.get_rectify_invoice_preview(x_property_id, get_rectify_invoice_note_preview_request)
        print("The response of FiscalDocumentsApi->get_rectify_invoice_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_rectify_invoice_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **get_rectify_invoice_note_preview_request** | [**GetRectifyInvoiceNotePreviewRequest**](GetRectifyInvoiceNotePreviewRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selected_transactions_summary**
> FiscalDocumentTransactionsSummary get_selected_transactions_summary(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, folio_ids=folio_ids, exclude_transaction_ids=exclude_transaction_ids, include_transaction_ids=include_transaction_ids, currency=currency)

Get totals of selected available transactions for fiscal documents (deprecated)

**Deprecated:** Use POST /fiscal-document/v1/fiscal-documents/transactions/summary instead.
Get totals of selected available transactions for fiscal documents based on the document type.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.models.fiscal_document_transactions_summary import FiscalDocumentTransactionsSummary
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    source_id = 56 # int | source ID.
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind.
    for_document_type = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related (deprecated, use `documentKind` instead). (optional)
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related. (optional)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)
    exclude_transaction_ids = [56] # List[int] | transaction IDs to exclude. (optional)
    include_transaction_ids = [56] # List[int] | transaction IDs to include. (optional)
    currency = 'currency_example' # str | Invoice currency to express the totals in. When provided, totals are converted from the property currency using the property's configured exchange rates. When omitted, totals are returned in the property currency. (optional)

    try:
        # Get totals of selected available transactions for fiscal documents (deprecated)
        api_response = api_instance.get_selected_transactions_summary(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, folio_ids=folio_ids, exclude_transaction_ids=exclude_transaction_ids, include_transaction_ids=include_transaction_ids, currency=currency)
        print("The response of FiscalDocumentsApi->get_selected_transactions_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_selected_transactions_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_id** | **int**| source ID. | 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | 
 **for_document_type** | [**FiscalDocumentKind**](.md)| Document type for which transactions are related (deprecated, use &#x60;documentKind&#x60; instead). | [optional] 
 **document_kind** | [**FiscalDocumentKind**](.md)| Document type for which transactions are related. | [optional] 
 **folio_ids** | [**List[int]**](int.md)| Filter by folio IDs. | [optional] 
 **exclude_transaction_ids** | [**List[int]**](int.md)| transaction IDs to exclude. | [optional] 
 **include_transaction_ids** | [**List[int]**](int.md)| transaction IDs to include. | [optional] 
 **currency** | **str**| Invoice currency to express the totals in. When provided, totals are converted from the property currency using the property&#39;s configured exchange rates. When omitted, totals are returned in the property currency. | [optional] 

### Return type

[**FiscalDocumentTransactionsSummary**](FiscalDocumentTransactionsSummary.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_summary_by_document_id**
> FiscalDocumentTransactionsSummary get_transactions_summary_by_document_id(id, x_property_id, include_linked_document_transactions=include_linked_document_transactions)

Get totals of transactions for a given fiscal document id

Get totals of transactions for a given fiscal document id.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_summary import FiscalDocumentTransactionsSummary
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 'id_example' # str | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id
    include_linked_document_transactions = False # bool | Include transactions from linked documents. (optional) (default to False)

    try:
        # Get totals of transactions for a given fiscal document id
        api_response = api_instance.get_transactions_summary_by_document_id(id, x_property_id, include_linked_document_transactions=include_linked_document_transactions)
        print("The response of FiscalDocumentsApi->get_transactions_summary_by_document_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_transactions_summary_by_document_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 
 **include_linked_document_transactions** | **bool**| Include transactions from linked documents. | [optional] [default to False]

### Return type

[**FiscalDocumentTransactionsSummary**](FiscalDocumentTransactionsSummary.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | The document&#39;s transactions are being reconciled. The totals are not safe to act on yet — retry the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_selected_transactions_summary**
> FiscalDocumentTransactionsSummary post_selected_transactions_summary(x_property_id, transactions_summary_request)

Get totals of selected available transactions for fiscal documents

Get totals of selected available transactions for fiscal documents based on the document type.
Supports partial transaction amounts via transactionIdToAmount.


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_summary import FiscalDocumentTransactionsSummary
from cloudbeds_fiscal_document.models.transactions_summary_request import TransactionsSummaryRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    transactions_summary_request = cloudbeds_fiscal_document.TransactionsSummaryRequest() # TransactionsSummaryRequest | 

    try:
        # Get totals of selected available transactions for fiscal documents
        api_response = api_instance.post_selected_transactions_summary(x_property_id, transactions_summary_request)
        print("The response of FiscalDocumentsApi->post_selected_transactions_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->post_selected_transactions_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **transactions_summary_request** | [**TransactionsSummaryRequest**](TransactionsSummaryRequest.md)|  | 

### Return type

[**FiscalDocumentTransactionsSummary**](FiscalDocumentTransactionsSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fiscal_document**
> FiscalDocumentSummaryResponse put_fiscal_document(id, x_property_id, fiscal_document_patch_request)

Update a fiscal document by id

Update a fiscal document status, government integration details, or failure reason.
Used by integration partners to update document lifecycle and government processing status.

**Common Updates:**
- Update status (PENDING_INTEGRATION, COMPLETED_INTEGRATION, FAILED, etc.)
- Set government integration details (series, number, external ID, QR codes)
- Record failure reasons for failed integrations

**Invoice Cancellation (Spanish Properties Only):**
- Set status to CANCEL_REQUESTED to cancel invoices
- Only invoices in OPEN, PAID, PARTIALLY_PAID or CORRECTION_NEEDED status can be canceled
- Invoices with rectifying documents cannot be canceled
- Integration partners must handle CANCEL_REQUESTED and update to CANCELED (success) or revert to previous status (failure)


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_patch_request import FiscalDocumentPatchRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 56 # int | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id
    fiscal_document_patch_request = cloudbeds_fiscal_document.FiscalDocumentPatchRequest() # FiscalDocumentPatchRequest | 

    try:
        # Update a fiscal document by id
        api_response = api_instance.put_fiscal_document(id, x_property_id, fiscal_document_patch_request)
        print("The response of FiscalDocumentsApi->put_fiscal_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->put_fiscal_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 
 **fiscal_document_patch_request** | [**FiscalDocumentPatchRequest**](FiscalDocumentPatchRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pro_forma_invoice_status**
> FiscalDocumentSummaryResponse update_pro_forma_invoice_status(id, x_property_id, pro_forma_status_update_request)

Update pro forma invoice status

Update the status of a pro forma invoice. Supported status transitions:
- OPEN -> ACCEPTED, REJECTED, CANCELED
- ACCEPTED -> CANCELED
- REJECTED -> CANCELED


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.pro_forma_status_update_request import ProFormaStatusUpdateRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 56 # int | Unique ID of the pro forma invoice to update.
    x_property_id = 56 # int | Property id
    pro_forma_status_update_request = cloudbeds_fiscal_document.ProFormaStatusUpdateRequest() # ProFormaStatusUpdateRequest | 

    try:
        # Update pro forma invoice status
        api_response = api_instance.update_pro_forma_invoice_status(id, x_property_id, pro_forma_status_update_request)
        print("The response of FiscalDocumentsApi->update_pro_forma_invoice_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->update_pro_forma_invoice_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID of the pro forma invoice to update. | 
 **x_property_id** | **int**| Property id | 
 **pro_forma_status_update_request** | [**ProFormaStatusUpdateRequest**](ProFormaStatusUpdateRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pro forma invoice status successfully updated |  -  |
**400** | Bad Request - Invalid status or document type |  -  |
**404** | Pro forma invoice not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_require_attention**
> FiscalDocumentSummaryResponse update_require_attention(id, x_property_id, update_require_attention_request)

Update require attention flag for a fiscal document

Sets the requireAttention flag on a fiscal document.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.update_require_attention_request import UpdateRequireAttentionRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    id = 'id_example' # str | Unique ID of the fiscal document to download.
    x_property_id = 56 # int | Property id
    update_require_attention_request = cloudbeds_fiscal_document.UpdateRequireAttentionRequest() # UpdateRequireAttentionRequest | 

    try:
        # Update require attention flag for a fiscal document
        api_response = api_instance.update_require_attention(id, x_property_id, update_require_attention_request)
        print("The response of FiscalDocumentsApi->update_require_attention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->update_require_attention: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the fiscal document to download. | 
 **x_property_id** | **int**| Property id | 
 **update_require_attention_request** | [**UpdateRequireAttentionRequest**](UpdateRequireAttentionRequest.md)|  | 

### Return type

[**FiscalDocumentSummaryResponse**](FiscalDocumentSummaryResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Fiscal document not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_receipt**
> void_receipt(x_property_id, receipt_id, void_receipt_request=void_receipt_request)

Void a receipt

Voids a receipt by updating its status to VOIDED.
The receipt must be in OPEN status.
For Italy, a refund receipt will be automatically created and linked to the voided receipt.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.void_receipt_request import VoidReceiptRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalDocumentsApi(api_client)
    x_property_id = 56 # int | Property id
    receipt_id = 56 # int | The ID of the receipt to void
    void_receipt_request = cloudbeds_fiscal_document.VoidReceiptRequest() # VoidReceiptRequest |  (optional)

    try:
        # Void a receipt
        api_instance.void_receipt(x_property_id, receipt_id, void_receipt_request=void_receipt_request)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->void_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **receipt_id** | **int**| The ID of the receipt to void | 
 **void_receipt_request** | [**VoidReceiptRequest**](VoidReceiptRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Receipt successfully voided |  -  |
**400** | Bad Request - Invalid status or document type |  -  |
**404** | Receipt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

