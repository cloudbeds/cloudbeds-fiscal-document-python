# cloudbeds_fiscal_document.FiscalDocumentsApi

All URIs are relative to *http://localhost:8700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit_note**](FiscalDocumentsApi.md#create_credit_note) | **POST** /fiscal-document/v1/fiscal-documents/credit-note | Create a fiscal document of the type credit note
[**create_invoice**](FiscalDocumentsApi.md#create_invoice) | **POST** /fiscal-document/v1/fiscal-documents/invoice | Create a fiscal document of the type invoice
[**download_fiscal_document**](FiscalDocumentsApi.md#download_fiscal_document) | **GET** /fiscal-document/v1/fiscal-documents/{id}/download | Download fiscal document
[**email_fiscal_document**](FiscalDocumentsApi.md#email_fiscal_document) | **POST** /fiscal-document/v1/fiscal-documents/{id}/email | Email a fiscal document
[**get_fiscal_document_recipients_by_id**](FiscalDocumentsApi.md#get_fiscal_document_recipients_by_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/recipients | Get list of recipients associated to the fiscal document
[**get_fiscal_document_transactions**](FiscalDocumentsApi.md#get_fiscal_document_transactions) | **GET** /fiscal-document/v1/fiscal-documents/transactions | Get list of fiscal documents
[**get_fiscal_document_transactions_by_id**](FiscalDocumentsApi.md#get_fiscal_document_transactions_by_id) | **GET** /fiscal-document/v1/fiscal-documents/{id}/transactions | Get list of transactions for a given fiscal document id
[**get_fiscal_documents**](FiscalDocumentsApi.md#get_fiscal_documents) | **GET** /fiscal-document/v1/fiscal-documents | Get list of fiscal documents
[**put_fiscal_document**](FiscalDocumentsApi.md#put_fiscal_document) | **PUT** /fiscal-document/v1/fiscal-documents/{id} | Update a fiscal document by id


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
> FiscalDocumentTransactionsPaginated get_fiscal_document_transactions(x_property_id, for_document_type, source_id, source_kind, page_token=page_token, limit=limit)

Get list of fiscal documents

Retrieves a paginated list of available transactions for source.

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
    for_document_type = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | Document type for which transactions are related.
    source_id = 56 # int | source ID.
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind.
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)

    try:
        # Get list of fiscal documents
        api_response = api_instance.get_fiscal_document_transactions(x_property_id, for_document_type, source_id, source_kind, page_token=page_token, limit=limit)
        print("The response of FiscalDocumentsApi->get_fiscal_document_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalDocumentsApi->get_fiscal_document_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **for_document_type** | [**FiscalDocumentKind**](.md)| Document type for which transactions are related. | 
 **source_id** | **int**| source ID. | 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | 
 **page_token** | **str**| Token for fetching the next page, as per cursor-based pagination. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]

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
> FiscalDocumentTransactionsPaginated get_fiscal_document_transactions_by_id(id, x_property_id, page_token=page_token, limit=limit)

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
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)

    try:
        # Get list of transactions for a given fiscal document id
        api_response = api_instance.get_fiscal_document_transactions_by_id(id, x_property_id, page_token=page_token, limit=limit)
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
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]

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

# **get_fiscal_documents**
> FiscalDocumentPaginated get_fiscal_documents(x_property_id, page_token=page_token, sort=sort, limit=limit, ids=ids, source_ids=source_ids, source_identifiers=source_identifiers, source_kind=source_kind, statuses=statuses, kinds=kinds)

Get list of fiscal documents

Retrieves a paginated list of fiscal documents filtered by optional criteria.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
from cloudbeds_fiscal_document.models.fiscal_document_paginated import FiscalDocumentPaginated
from cloudbeds_fiscal_document.models.fiscal_document_status import FiscalDocumentStatus
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
    page_token = 'page_token_example' # str | Token for fetching the next page, as per cursor-based pagination. (optional)
    sort = 'createdAt:desc' # str | Supported fields createdAt. Supported sort modes asc:desc If not supplied default is asc. (optional)
    limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    ids = ['[\"123\",\"456\",\"789\"]'] # List[str] | Comma-separated list of IDs. (optional)
    source_ids = ['[\"123\",\"456\",\"789\"]'] # List[str] | Comma-separated list of source IDs. (optional)
    source_identifiers = ['[\"ABC123\",\"XYZ789\"]'] # List[str] | Comma-separated list of source-specific identifiers. (optional)
    source_kind = cloudbeds_fiscal_document.SourceKind() # SourceKind | Filter by source kind. (optional)
    statuses = [cloudbeds_fiscal_document.FiscalDocumentStatus()] # List[FiscalDocumentStatus] | Comma-separated list of fiscal document statuses. (optional)
    kinds = [cloudbeds_fiscal_document.FiscalDocumentKind()] # List[FiscalDocumentKind] | Comma-separated list of fiscal document kinds. (optional)

    try:
        # Get list of fiscal documents
        api_response = api_instance.get_fiscal_documents(x_property_id, page_token=page_token, sort=sort, limit=limit, ids=ids, source_ids=source_ids, source_identifiers=source_identifiers, source_kind=source_kind, statuses=statuses, kinds=kinds)
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
 **sort** | **str**| Supported fields createdAt. Supported sort modes asc:desc If not supplied default is asc. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **ids** | [**List[str]**](str.md)| Comma-separated list of IDs. | [optional] 
 **source_ids** | [**List[str]**](str.md)| Comma-separated list of source IDs. | [optional] 
 **source_identifiers** | [**List[str]**](str.md)| Comma-separated list of source-specific identifiers. | [optional] 
 **source_kind** | [**SourceKind**](.md)| Filter by source kind. | [optional] 
 **statuses** | [**List[FiscalDocumentStatus]**](FiscalDocumentStatus.md)| Comma-separated list of fiscal document statuses. | [optional] 
 **kinds** | [**List[FiscalDocumentKind]**](FiscalDocumentKind.md)| Comma-separated list of fiscal document kinds. | [optional] 

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

# **put_fiscal_document**
> FiscalDocumentSummaryResponse put_fiscal_document(id, x_property_id, fiscal_document_patch_request)

Update a fiscal document by id

Endpoint to update a fiscal document by id. Used for integrations partners for fiscalized countries.

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

