# cloudbeds_fiscal_document.FiscalDocumentsApi

All URIs are relative to *http://localhost:8700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_receipt_payment**](FiscalDocumentsApi.md#allocate_receipt_payment) | **POST** /fiscal-document/v1/fiscal-documents/receipt/allocate-payment | Allocate payment associated with receipt to charge transactions.
[**create_credit_note**](FiscalDocumentsApi.md#create_credit_note) | **POST** /fiscal-document/v1/fiscal-documents/credit-note | Create a fiscal document of the type credit note
[**create_invoice**](FiscalDocumentsApi.md#create_invoice) | **POST** /fiscal-document/v1/fiscal-documents/invoice | Create a fiscal document of the type invoice
[**create_pro_forma_invoice**](FiscalDocumentsApi.md#create_pro_forma_invoice) | **POST** /fiscal-document/v1/fiscal-documents/pro-forma-invoice | Create a fiscal document of the type pro forma invoice
[**create_receipt**](FiscalDocumentsApi.md#create_receipt) | **POST** /fiscal-document/v1/fiscal-documents/receipt | Create receipt for a payment.
[**create_rectify_invoice**](FiscalDocumentsApi.md#create_rectify_invoice) | **POST** /fiscal-document/v1/fiscal-documents/rectify-invoice | Create a fiscal document of the type rectify invoice
[**create_simple_receipt**](FiscalDocumentsApi.md#create_simple_receipt) | **POST** /fiscal-document/v1/fiscal-documents/simple-receipt | Create simple receipts.
[**download_fiscal_document**](FiscalDocumentsApi.md#download_fiscal_document) | **GET** /fiscal-document/v1/fiscal-documents/{id}/download | Download fiscal document
[**email_fiscal_document**](FiscalDocumentsApi.md#email_fiscal_document) | **POST** /fiscal-document/v1/fiscal-documents/{id}/email | Email a fiscal document
[**get_allocations**](FiscalDocumentsApi.md#get_allocations) | **GET** /fiscal-document/v1/fiscal-documents/allocations | Get payment allocation transactions
[**get_allocations_summary**](FiscalDocumentsApi.md#get_allocations_summary) | **GET** /fiscal-document/v1/fiscal-documents/allocations/summary | Get allocations summary
[**get_credit_note_preview**](FiscalDocumentsApi.md#get_credit_note_preview) | **POST** /fiscal-document/v1/fiscal-documents/credit-note/preview | Get fiscal document preview of the type credit note
[**get_document_preview**](FiscalDocumentsApi.md#get_document_preview) | **POST** /fiscal-document/v1/fiscal-documents/invoice/preview | Get fiscal document preview of the type invoice
[**get_fiscal_document_recipients_by_id**](FiscalDocumentsApi.md#get_fiscal_document_recipients_by_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/recipients | Get list of recipients associated to the fiscal document
[**get_fiscal_document_transactions**](FiscalDocumentsApi.md#get_fiscal_document_transactions) | **GET** /fiscal-document/v1/fiscal-documents/transactions | Get available transactions for fiscal documents
[**get_fiscal_document_transactions_by_id**](FiscalDocumentsApi.md#get_fiscal_document_transactions_by_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/transactions | Get list of transactions for a given fiscal document id
[**get_fiscal_document_transactions_for_allocation**](FiscalDocumentsApi.md#get_fiscal_document_transactions_for_allocation) | **GET** /fiscal-document/v1/fiscal-documents/allocations/transactions | Get available transactions for allocations
[**get_fiscal_documents**](FiscalDocumentsApi.md#get_fiscal_documents) | **GET** /fiscal-document/v1/fiscal-documents | Get list of fiscal documents
[**get_pro_forma_preview**](FiscalDocumentsApi.md#get_pro_forma_preview) | **POST** /fiscal-document/v1/fiscal-documents/pro-forma-invoice/preview | Create a fiscal document of the type pro forma invoice
[**get_rectify_invoice_preview**](FiscalDocumentsApi.md#get_rectify_invoice_preview) | **POST** /fiscal-document/v1/fiscal-documents/rectify-invoice/preview | Get fiscal document preview of the type rectify invoice
[**get_selected_transactions_summary**](FiscalDocumentsApi.md#get_selected_transactions_summary) | **GET** /fiscal-document/v1/fiscal-documents/transactions/summary | Get totals of selected available transactions for fiscal documents
[**get_transactions_summary_by_document_id**](FiscalDocumentsApi.md#get_transactions_summary_by_document_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/transactions/summary | Get totals of transactions for a given fiscal document id
[**put_fiscal_document**](FiscalDocumentsApi.md#put_fiscal_document) | **PUT** /fiscal-document/v1/fiscal-documents/{id} | Update a fiscal document by id
[**update_pro_forma_invoice_status**](FiscalDocumentsApi.md#update_pro_forma_invoice_status) | **PUT** /fiscal-document/v1/fiscal-documents/pro-forma-invoice/{id}/status | Update pro forma invoice status


# **allocate_receipt_payment**
> FiscalDocumentSummaryResponse allocate_receipt_payment(x_property_id, allocate_receipt_payment_request)

Allocate payment associated with receipt to charge transactions.

Allocate payment associated with receipt to charge transactions. The amounts of all allocations must be equal to the payment amount. The transactions should not be fully allocated already   and the amount allocated should not be more than the remaining balance on the transaction. All transactions not part of an invoice will be added to newly created invoice. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.allocate_receipt_payment_request import AllocateReceiptPaymentRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

# **create_credit_note**
> FiscalDocumentSummaryResponse create_credit_note(x_property_id, create_credit_note_request)

Create a fiscal document of the type credit note

Create a fiscal document of the type credit note.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_credit_note_request import CreateCreditNoteRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice**
> FiscalDocumentSummaryResponse create_invoice(x_property_id, create_invoice_request)

Create a fiscal document of the type invoice

Create a fiscal document of the type invoice.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_invoice_request import CreateInvoiceRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

Create a fiscal document of the type pro forma invoice.  **Pro Forma Invoice Characteristics:** - Contains pending transactions that are subject to change - Includes payment information - Transactions are NOT locked (unlike regular invoices) - Can be converted to regular invoices later when transactions are posted - Has its own sequence numbering and settings 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.pro_forma_invoice_request import ProFormaInvoiceRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

Create a receipt for a payment and optionally specify allocations per transaction. In case of no allocations, a 'Simple receipt' will be created that can later be allocated to charge transactions. The amounts of all allocations must be equal to the payment amount. The transactions should not be fully allocated already   and the amount allocated should not be more than the remaining balance on the transaction. All transactions not part of an invoice will be added to newly created invoice. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_receipt_request import CreateReceiptRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

Create a fiscal document of the type rectify invoice.  **Spanish Fiscal Regulations:** - Only available for properties in Spain - An invoice that has already been rectified cannot be rectified again - To make corrections to a rectified invoice, you must rectify the most recent invoice in the rectification chain  **Validation Rules:** - The target invoice must not have been previously rectified - If the invoice has been rectified, the API will return an error with details about which invoice should be rectified instead 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.rectify_invoice_note_request import RectifyInvoiceNoteRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Validation errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_simple_receipt**
> List[FiscalDocumentSummaryResponse] create_simple_receipt(x_property_id, create_simple_receipt_request)

Create simple receipts.

Create receipts for list of payments without allocations. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.create_simple_receipt_request import CreateSimpleReceiptRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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
> bytearray download_fiscal_document(id, x_property_id)

Download fiscal document

Initiates the download of the fiscal document file

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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
        # Download fiscal document
        api_response = api_instance.download_fiscal_document(id, x_property_id)
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

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_fiscal_document**
> object email_fiscal_document(id, x_property_id, fiscal_document_email_request)

Email a fiscal document

Initiates the process to send the invoice to a customer

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_email_request import FiscalDocumentEmailRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.allocations_data import AllocationsData
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

# **get_credit_note_preview**
> bytearray get_credit_note_preview(x_property_id, get_credit_note_preview_request)

Get fiscal document preview of the type credit note

Get fiscal document preview of the type credit note.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_credit_note_preview_request import GetCreditNotePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_invoice_preview_request import GetInvoicePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

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

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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
> FiscalDocumentTransactionsPaginated get_fiscal_document_transactions(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids)

Get available transactions for fiscal documents

Retrieves a paginated list of available transactions for a source based on the document type. - For INVOICE: Returns only posted (paid) transactions - For PRO_FORMA_INVOICE: Returns both pending transactions and posted (paid) payments - Transactions already included in fiscal documents are excluded - Each transaction includes a status field (PENDING or POSTED) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.models.fiscal_document_transactions_paginated import FiscalDocumentTransactionsPaginated
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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
    for_document_type = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related (deprecated, use `documentKind` instead). (optional)
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related. (optional)
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    sort = 'createdAt:desc' # str | Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode (optional)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)

    try:
        # Get available transactions for fiscal documents
        api_response = api_instance.get_fiscal_document_transactions(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids)
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

### Return type

[**FiscalDocumentTransactionsPaginated**](FiscalDocumentTransactionsPaginated.md)

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

# **get_fiscal_document_transactions_by_id**
> FiscalDocumentTransactionsPaginated get_fiscal_document_transactions_by_id(id, x_property_id, page_token=page_token, include_linked_document_transactions=include_linked_document_transactions, sort=sort, limit=limit, folio_ids=folio_ids)

Get list of transactions for a given fiscal document id

Retrieves a paginated list of available transactions for fiscal document id.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_paginated import FiscalDocumentTransactionsPaginated
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    include_linked_document_transactions = False # bool | Include transactions from linked documents. (optional) (default to False)
    sort = 'createdAt:desc' # str | Supported fields - createdAt, serviceDate, sourceId, transactionDate, internalCode (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)

    try:
        # Get list of transactions for a given fiscal document id
        api_response = api_instance.get_fiscal_document_transactions_by_id(id, x_property_id, page_token=page_token, include_linked_document_transactions=include_linked_document_transactions, sort=sort, limit=limit, folio_ids=folio_ids)
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

### Return type

[**FiscalDocumentTransactionsPaginated**](FiscalDocumentTransactionsPaginated.md)

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

# **get_fiscal_document_transactions_for_allocation**
> FiscalDocumentTransactionsForAllocationPaginated get_fiscal_document_transactions_for_allocation(x_property_id, source_id, source_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids, document_ids=document_ids)

Get available transactions for allocations

Retrieves a paginated list of available transactions for allocations. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_for_allocation_paginated import FiscalDocumentTransactionsForAllocationPaginated
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

    try:
        # Get available transactions for allocations
        api_response = api_instance.get_fiscal_document_transactions_for_allocation(x_property_id, source_id, source_kind, page_token=page_token, limit=limit, sort=sort, folio_ids=folio_ids, document_ids=document_ids)
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

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_filters import FiscalDocumentFilters
from cloudbeds_fiscal_document.models.fiscal_document_paginated import FiscalDocumentPaginated
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pro_forma_preview**
> bytearray get_pro_forma_preview(x_property_id, pro_forma_invoice_preview_request)

Create a fiscal document of the type pro forma invoice

Create a fiscal document of the type pro forma invoice.  **Pro Forma Invoice Characteristics:** - Contains pending transactions that are subject to change - Includes payment information - Transactions are NOT locked (unlike regular invoices) - Can be converted to regular invoices later when transactions are posted - Has its own sequence numbering and settings 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.pro_forma_invoice_preview_request import ProFormaInvoicePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

Get fiscal document preview of the type rectify invoice. **Spanish Fiscal Regulations:** - Only available for properties in Spain - An invoice that has already been rectified cannot be rectified again - To make corrections to a rectified invoice, you must rectify the most recent invoice in the rectification chain **Validation Rules:** - The target invoice must not have been previously rectified - If the invoice has been rectified, the API will return an error with details about which invoice should be rectified instead 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_rectify_invoice_note_preview_request import GetRectifyInvoiceNotePreviewRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful file download |  * Content-Disposition - Used to indicate if the content should be displayed inline or as an attachment. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selected_transactions_summary**
> FiscalDocumentTransactionsSummary get_selected_transactions_summary(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, folio_ids=folio_ids, exclude_transaction_ids=exclude_transaction_ids, include_transaction_ids=include_transaction_ids)

Get totals of selected available transactions for fiscal documents

Get totals of selected available transactions for fiscal documents based on the document type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.models.fiscal_document_transactions_summary import FiscalDocumentTransactionsSummary
from cloudbeds_fiscal_document.models.source_kind import SourceKind
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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
    for_document_type = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related (deprecated, use `documentKind` instead). (optional)
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related. (optional)
    folio_ids = [56] # List[int] | Filter by folio IDs. (optional)
    exclude_transaction_ids = [56] # List[int] | transaction IDs to exclude. (optional)
    include_transaction_ids = [56] # List[int] | transaction IDs to include. (optional)

    try:
        # Get totals of selected available transactions for fiscal documents
        api_response = api_instance.get_selected_transactions_summary(x_property_id, source_id, source_kind, for_document_type=for_document_type, document_kind=document_kind, folio_ids=folio_ids, exclude_transaction_ids=exclude_transaction_ids, include_transaction_ids=include_transaction_ids)
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

### Return type

[**FiscalDocumentTransactionsSummary**](FiscalDocumentTransactionsSummary.md)

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

# **get_transactions_summary_by_document_id**
> FiscalDocumentTransactionsSummary get_transactions_summary_by_document_id(id, x_property_id, include_linked_document_transactions=include_linked_document_transactions)

Get totals of transactions for a given fiscal document id

Get totals of transactions for a given fiscal document id.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_transactions_summary import FiscalDocumentTransactionsSummary
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fiscal_document**
> FiscalDocumentSummaryResponse put_fiscal_document(id, x_property_id, fiscal_document_patch_request)

Update a fiscal document by id

Update a fiscal document status, government integration details, or failure reason. Used by integration partners to update document lifecycle and government processing status.  **Common Updates:** - Update status (PENDING_INTEGRATION, COMPLETED_INTEGRATION, FAILED, etc.) - Set government integration details (series, number, external ID, QR codes) - Record failure reasons for failed integrations  **Invoice Cancellation (Spanish Properties Only):** - Set status to CANCEL_REQUESTED to cancel invoices - Only invoices in OPEN, PAID, PARTIALLY_PAID or CORRECTION_NEEDED status can be canceled - Invoices with rectifying documents cannot be canceled - Integration partners must handle CANCEL_REQUESTED and update to CANCELED (success) or revert to previous status (failure) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_patch_request import FiscalDocumentPatchRequest
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

Update the status of a pro forma invoice. Supported status transitions: - OPEN -> ACCEPTED, REJECTED, CANCELED - ACCEPTED -> CANCELED - REJECTED -> CANCELED 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_summary_response import FiscalDocumentSummaryResponse
from cloudbeds_fiscal_document.models.pro_forma_status_update_request import ProFormaStatusUpdateRequest
from cloudbeds_fiscal_document.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8700
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_fiscal_document.Configuration(
    host = "http://localhost:8700"
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

[bearerAuth](../README.md#bearerAuth)

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

