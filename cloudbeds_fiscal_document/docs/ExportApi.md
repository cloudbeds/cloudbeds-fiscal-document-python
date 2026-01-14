# cloudbeds_fiscal_document.ExportApi

All URIs are relative to *http://localhost:8700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_folio_pdf**](ExportApi.md#get_folio_pdf) | **POST** /fiscal-document/v1/folio-export/pdf | Get folio list of transactions exported as PDF


# **get_folio_pdf**
> bytearray get_folio_pdf(x_property_id, get_folio_export_request, accept_language=accept_language)

Get folio list of transactions exported as PDF

Get folio list of transactions exported as PDF

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_folio_export_request import GetFolioExportRequest
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
    api_instance = cloudbeds_fiscal_document.ExportApi(api_client)
    x_property_id = 56 # int | Property id
    get_folio_export_request = cloudbeds_fiscal_document.GetFolioExportRequest() # GetFolioExportRequest | 
    accept_language = 'accept_language_example' # str | Desired language of exported PDF (optional)

    try:
        # Get folio list of transactions exported as PDF
        api_response = api_instance.get_folio_pdf(x_property_id, get_folio_export_request, accept_language=accept_language)
        print("The response of ExportApi->get_folio_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->get_folio_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **get_folio_export_request** | [**GetFolioExportRequest**](GetFolioExportRequest.md)|  | 
 **accept_language** | **str**| Desired language of exported PDF | [optional] 

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

