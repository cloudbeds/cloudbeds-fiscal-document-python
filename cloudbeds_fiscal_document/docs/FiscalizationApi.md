# cloudbeds_fiscal_document.FiscalizationApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connection_report**](FiscalizationApi.md#get_connection_report) | **GET** /fiscal-document/v1/fiscalization/connections/{connectionId}/reports/{reportId} | Generate and download a report for one connection
[**get_fiscalization_item_extension_rules**](FiscalizationApi.md#get_fiscalization_item_extension_rules) | **GET** /fiscal-document/v1/fiscalization/items/rules | Get item extension mapping rules for a country
[**get_fiscalization_payment_method_rules**](FiscalizationApi.md#get_fiscalization_payment_method_rules) | **GET** /fiscal-document/v1/fiscalization/payment-methods/rules | Get fiscalization payment method rules for a country
[**get_fiscalization_registration_rules**](FiscalizationApi.md#get_fiscalization_registration_rules) | **GET** /fiscal-document/v1/fiscalization/registration/rules | Get fiscalization rules for a country
[**get_fiscalization_report**](FiscalizationApi.md#get_fiscalization_report) | **GET** /fiscal-document/v1/fiscalization/reports/{reportId} | Generate and download a fiscalization report
[**get_fiscalization_series_rules**](FiscalizationApi.md#get_fiscalization_series_rules) | **GET** /fiscal-document/v1/fiscalization/series/rules | Get available series rules for a country
[**get_fiscalization_tax_rules**](FiscalizationApi.md#get_fiscalization_tax_rules) | **GET** /fiscal-document/v1/fiscalization/tax/rules | Get fiscalization tax rules for a country
[**get_invoice_type_options**](FiscalizationApi.md#get_invoice_type_options) | **GET** /fiscal-document/v1/fiscalization/invoice-type-options | Get invoicing options for a property


# **get_connection_report**
> bytearray get_connection_report(x_property_id, connection_id, report_id, year, period=period)

Generate and download a report for one connection

Generates a country-specific report (e.g. SAF-T for Portugal) from the registration behind the given connection. Reports are a per-connection section, so a property holding more than one connection gets a distinct report per connection.

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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    report_id = 'report_id_example' # str | Report identifier (e.g., \"saft\")
    year = 56 # int | Report year
    period = 0 # int | Report period (1-12 for monthly, 0 for full year) (optional) (default to 0)

    try:
        # Generate and download a report for one connection
        api_response = api_instance.get_connection_report(x_property_id, connection_id, report_id, year, period=period)
        print("The response of FiscalizationApi->get_connection_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_connection_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **report_id** | **str**| Report identifier (e.g., \&quot;saft\&quot;) | 
 **year** | **int**| Report year | 
 **period** | **int**| Report period (1-12 for monthly, 0 for full year) | [optional] [default to 0]

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report generated successfully |  * Content-Disposition -  <br>  |
**400** | Invalid parameters |  -  |
**404** | Connection not registered or report not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_item_extension_rules**
> ItemExtensionRulesResponse get_fiscalization_item_extension_rules(country)

Get item extension mapping rules for a country

Returns country-specific item categories and GOBL extension fields for per-item mapping

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.item_extension_rules_response import ItemExtensionRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., BR, MX)

    try:
        # Get item extension mapping rules for a country
        api_response = api_instance.get_fiscalization_item_extension_rules(country)
        print("The response of FiscalizationApi->get_fiscalization_item_extension_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_item_extension_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., BR, MX) | 

### Return type

[**ItemExtensionRulesResponse**](ItemExtensionRulesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved item extension rules |  -  |
**400** | Invalid country code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_payment_method_rules**
> PaymentMethodRulesResponse get_fiscalization_payment_method_rules(country)

Get fiscalization payment method rules for a country

Returns country-specific GOBL payment means keys for configuring payment method mappings

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.payment_method_rules_response import PaymentMethodRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., PT, IT, MX)

    try:
        # Get fiscalization payment method rules for a country
        api_response = api_instance.get_fiscalization_payment_method_rules(country)
        print("The response of FiscalizationApi->get_fiscalization_payment_method_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_payment_method_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., PT, IT, MX) | 

### Return type

[**PaymentMethodRulesResponse**](PaymentMethodRulesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved payment method rules |  -  |
**400** | Invalid country code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_registration_rules**
> FiscalizationRegistrationRulesResponse get_fiscalization_registration_rules(country, section_key=section_key, channel_code=channel_code)

Get fiscalization rules for a country

Returns country-specific fiscalization rules for building forms. The response always includes the full section list; `fields` is filtered by the optional `sectionKey` query param (default `registration`).

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_rules_response import FiscalizationRegistrationRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX)
    section_key = 'registration' # str | Filter `fields` to the given section. Default `registration`. Pass the key of any section declared in the rules (e.g. `customization.invoicing`) to fetch its fields only. (optional) (default to 'registration')
    channel_code = 'channel_code_example' # str | Fiscal channel to scope the rules and requirements to (e.g. `SR` for Italy Smart Receipts / Documento Commerciale). Omit for the default channel (e.g. Italy SDI / FatturaPA); unknown channels fall back to the country's default rules. (optional)

    try:
        # Get fiscalization rules for a country
        api_response = api_instance.get_fiscalization_registration_rules(country, section_key=section_key, channel_code=channel_code)
        print("The response of FiscalizationApi->get_fiscalization_registration_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_registration_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX) | 
 **section_key** | **str**| Filter &#x60;fields&#x60; to the given section. Default &#x60;registration&#x60;. Pass the key of any section declared in the rules (e.g. &#x60;customization.invoicing&#x60;) to fetch its fields only. | [optional] [default to &#39;registration&#39;]
 **channel_code** | **str**| Fiscal channel to scope the rules and requirements to (e.g. &#x60;SR&#x60; for Italy Smart Receipts / Documento Commerciale). Omit for the default channel (e.g. Italy SDI / FatturaPA); unknown channels fall back to the country&#39;s default rules. | [optional] 

### Return type

[**FiscalizationRegistrationRulesResponse**](FiscalizationRegistrationRulesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved fiscalization rules |  -  |
**400** | Invalid country code |  -  |
**404** | Rules not found for country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_report**
> bytearray get_fiscalization_report(x_property_id, report_id, year, period=period)

Generate and download a fiscalization report

Generates a country-specific report (e.g., SAF-T for Portugal) and returns it for download.

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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | Property ID
    report_id = 'report_id_example' # str | Report identifier (e.g., \"saft\")
    year = 56 # int | Report year
    period = 0 # int | Report period (1-12 for monthly, 0 for full year) (optional) (default to 0)

    try:
        # Generate and download a fiscalization report
        api_response = api_instance.get_fiscalization_report(x_property_id, report_id, year, period=period)
        print("The response of FiscalizationApi->get_fiscalization_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property ID | 
 **report_id** | **str**| Report identifier (e.g., \&quot;saft\&quot;) | 
 **year** | **int**| Report year | 
 **period** | **int**| Report period (1-12 for monthly, 0 for full year) | [optional] [default to 0]

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report generated successfully |  * Content-Disposition -  <br>  |
**400** | Invalid parameters |  -  |
**404** | Property not registered or report not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_series_rules**
> FiscalizationSeriesRulesResponse get_fiscalization_series_rules(country)

Get available series rules for a country

Returns the available document type prefixes and series types for the given country.
Used by the frontend to build the series registration UI.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_series_rules_response import FiscalizationSeriesRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., PT)

    try:
        # Get available series rules for a country
        api_response = api_instance.get_fiscalization_series_rules(country)
        print("The response of FiscalizationApi->get_fiscalization_series_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_series_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., PT) | 

### Return type

[**FiscalizationSeriesRulesResponse**](FiscalizationSeriesRulesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved series rules |  -  |
**400** | Invalid or unsupported country code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_tax_rules**
> FiscalizationTaxRulesResponse get_fiscalization_tax_rules(country, x_property_id)

Get fiscalization tax rules for a country

Returns country-specific tax categories and rates for configuring tax mappings

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_tax_rules_response import FiscalizationTaxRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX)
    x_property_id = 56 # int | 

    try:
        # Get fiscalization tax rules for a country
        api_response = api_instance.get_fiscalization_tax_rules(country, x_property_id)
        print("The response of FiscalizationApi->get_fiscalization_tax_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_tax_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX) | 
 **x_property_id** | **int**|  | 

### Return type

[**FiscalizationTaxRulesResponse**](FiscalizationTaxRulesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved tax rules |  -  |
**400** | Invalid country code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_type_options**
> InvoiceTypeOptionsResponse get_invoice_type_options(x_property_id)

Get invoicing options for a property

Invoice classes a property may choose between when issuing an invoice; empty when there is no choice to surface. Country-specific (currently Argentina Responsable Inscripto); the country is resolved from the property's fiscalization config.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.invoice_type_options_response import InvoiceTypeOptionsResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | 

    try:
        # Get invoicing options for a property
        api_response = api_instance.get_invoice_type_options(x_property_id)
        print("The response of FiscalizationApi->get_invoice_type_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_invoice_type_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**|  | 

### Return type

[**InvoiceTypeOptionsResponse**](InvoiceTypeOptionsResponse.md)

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

