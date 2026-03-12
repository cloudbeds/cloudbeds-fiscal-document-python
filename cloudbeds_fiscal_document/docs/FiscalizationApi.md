# cloudbeds_fiscal_document.FiscalizationApi

All URIs are relative to *http://localhost:8700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscalization_consent**](FiscalizationApi.md#create_fiscalization_consent) | **POST** /fiscal-document/v1/fiscalization/consent | Record user consent for fiscalization
[**create_fiscalization_registration**](FiscalizationApi.md#create_fiscalization_registration) | **POST** /fiscal-document/v1/fiscalization/registration | Create fiscalization registration
[**get_fiscalization_consent**](FiscalizationApi.md#get_fiscalization_consent) | **GET** /fiscal-document/v1/fiscalization/consent | Get consent status for a property
[**get_fiscalization_provider**](FiscalizationApi.md#get_fiscalization_provider) | **GET** /fiscal-document/v1/fiscalization/provider | Get fiscalization provider info for a country
[**get_fiscalization_registration**](FiscalizationApi.md#get_fiscalization_registration) | **GET** /fiscal-document/v1/fiscalization/registration | Get fiscalization registration for a property
[**get_fiscalization_registration_countries**](FiscalizationApi.md#get_fiscalization_registration_countries) | **GET** /fiscal-document/v1/fiscalization/registration/countries | Get available countries for property registration
[**get_fiscalization_registration_rules**](FiscalizationApi.md#get_fiscalization_registration_rules) | **GET** /fiscal-document/v1/fiscalization/registration/rules | Get fiscalization registration rules for a country
[**get_fiscalization_registration_status**](FiscalizationApi.md#get_fiscalization_registration_status) | **GET** /fiscal-document/v1/fiscalization/registration/status | Get registration status for a property
[**get_fiscalization_tax**](FiscalizationApi.md#get_fiscalization_tax) | **GET** /fiscal-document/v1/fiscalization/tax | Get fiscalization tax for a property
[**get_fiscalization_tax_rules**](FiscalizationApi.md#get_fiscalization_tax_rules) | **GET** /fiscal-document/v1/fiscalization/tax/rules | Get fiscalization tax rules for a country
[**update_fiscalization_registration**](FiscalizationApi.md#update_fiscalization_registration) | **PUT** /fiscal-document/v1/fiscalization/registration | Update fiscalization registration
[**update_fiscalization_tax**](FiscalizationApi.md#update_fiscalization_tax) | **PUT** /fiscal-document/v1/fiscalization/tax | Update fiscalization tax for a property
[**validate_fiscalization_data**](FiscalizationApi.md#validate_fiscalization_data) | **POST** /fiscal-document/v1/fiscalization/registration/validate | Validate fiscalization registration data


# **create_fiscalization_consent**
> FiscalizationConsentResponse create_fiscalization_consent(x_property_id, fiscalization_consent_request)

Record user consent for fiscalization

Records that the user has consented to sharing data with the fiscalization provider

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_consent_request import FiscalizationConsentRequest
from cloudbeds_fiscal_document.models.fiscalization_consent_response import FiscalizationConsentResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | Property ID
    fiscalization_consent_request = cloudbeds_fiscal_document.FiscalizationConsentRequest() # FiscalizationConsentRequest | 

    try:
        # Record user consent for fiscalization
        api_response = api_instance.create_fiscalization_consent(x_property_id, fiscalization_consent_request)
        print("The response of FiscalizationApi->create_fiscalization_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->create_fiscalization_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property ID | 
 **fiscalization_consent_request** | [**FiscalizationConsentRequest**](FiscalizationConsentRequest.md)|  | 

### Return type

[**FiscalizationConsentResponse**](FiscalizationConsentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consent recorded successfully |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fiscalization_registration**
> FiscalizationRegistrationResponse create_fiscalization_registration(x_property_id, fiscalization_registration_request)

Create fiscalization registration

Creates a new fiscalization registration (supplier/party info) for the given property.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_request import FiscalizationRegistrationRequest
from cloudbeds_fiscal_document.models.fiscalization_registration_response import FiscalizationRegistrationResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | 
    fiscalization_registration_request = cloudbeds_fiscal_document.FiscalizationRegistrationRequest() # FiscalizationRegistrationRequest | 

    try:
        # Create fiscalization registration
        api_response = api_instance.create_fiscalization_registration(x_property_id, fiscalization_registration_request)
        print("The response of FiscalizationApi->create_fiscalization_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->create_fiscalization_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**|  | 
 **fiscalization_registration_request** | [**FiscalizationRegistrationRequest**](FiscalizationRegistrationRequest.md)|  | 

### Return type

[**FiscalizationRegistrationResponse**](FiscalizationRegistrationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_consent**
> FiscalizationConsentResponse get_fiscalization_consent(x_property_id)

Get consent status for a property

Returns whether the property has consented to fiscalization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_consent_response import FiscalizationConsentResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | Property ID

    try:
        # Get consent status for a property
        api_response = api_instance.get_fiscalization_consent(x_property_id)
        print("The response of FiscalizationApi->get_fiscalization_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property ID | 

### Return type

[**FiscalizationConsentResponse**](FiscalizationConsentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consent status retrieved successfully |  -  |
**404** | No consent found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_provider**
> FiscalizationProviderInfo get_fiscalization_provider(country)

Get fiscalization provider info for a country

Returns which provider handles fiscal registration for a given country

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_provider_info import FiscalizationProviderInfo
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX)

    try:
        # Get fiscalization provider info for a country
        api_response = api_instance.get_fiscalization_provider(country)
        print("The response of FiscalizationApi->get_fiscalization_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX) | 

### Return type

[**FiscalizationProviderInfo**](FiscalizationProviderInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider info retrieved successfully |  -  |
**400** | No provider configured for this country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_registration**
> FiscalizationRegistrationResponse get_fiscalization_registration(x_property_id)

Get fiscalization registration for a property

Returns the fiscalization registration (supplier/party info) for the given property.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_response import FiscalizationRegistrationResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | 

    try:
        # Get fiscalization registration for a property
        api_response = api_instance.get_fiscalization_registration(x_property_id)
        print("The response of FiscalizationApi->get_fiscalization_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**|  | 

### Return type

[**FiscalizationRegistrationResponse**](FiscalizationRegistrationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_registration_countries**
> List[FiscalizationCountryOption] get_fiscalization_registration_countries(x_property_id)

Get available countries for property registration

Returns list of countries available for fiscalization based on property location

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_country_option import FiscalizationCountryOption
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | Property ID

    try:
        # Get available countries for property registration
        api_response = api_instance.get_fiscalization_registration_countries(x_property_id)
        print("The response of FiscalizationApi->get_fiscalization_registration_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_registration_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property ID | 

### Return type

[**List[FiscalizationCountryOption]**](FiscalizationCountryOption.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available countries retrieved successfully |  -  |
**404** | Property not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_registration_rules**
> FiscalizationRegistrationRulesResponse get_fiscalization_registration_rules(country)

Get fiscalization registration rules for a country

Returns country-specific fiscalization rules for building forms

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_rules_response import FiscalizationRegistrationRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX)

    try:
        # Get fiscalization registration rules for a country
        api_response = api_instance.get_fiscalization_registration_rules(country)
        print("The response of FiscalizationApi->get_fiscalization_registration_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_registration_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX) | 

### Return type

[**FiscalizationRegistrationRulesResponse**](FiscalizationRegistrationRulesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

# **get_fiscalization_registration_status**
> FiscalizationRegistrationStatus get_fiscalization_registration_status(x_property_id)

Get registration status for a property

Returns the registration status with government systems for each configured country

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_status import FiscalizationRegistrationStatus
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | Property ID

    try:
        # Get registration status for a property
        api_response = api_instance.get_fiscalization_registration_status(x_property_id)
        print("The response of FiscalizationApi->get_fiscalization_registration_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_registration_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property ID | 

### Return type

[**FiscalizationRegistrationStatus**](FiscalizationRegistrationStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registration status retrieved successfully |  -  |
**404** | Property not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_tax**
> FiscalizationTaxResponse get_fiscalization_tax(x_property_id)

Get fiscalization tax for a property

Returns the fiscalization tax configuration for the given property

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_tax_response import FiscalizationTaxResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | 

    try:
        # Get fiscalization tax for a property
        api_response = api_instance.get_fiscalization_tax(x_property_id)
        print("The response of FiscalizationApi->get_fiscalization_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**|  | 

### Return type

[**FiscalizationTaxResponse**](FiscalizationTaxResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Fiscalization tax config not found for property |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscalization_tax_rules**
> FiscalizationTaxRulesResponse get_fiscalization_tax_rules(country)

Get fiscalization tax rules for a country

Returns country-specific tax categories and rates for configuring tax mappings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_tax_rules_response import FiscalizationTaxRulesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    country = 'country_example' # str | ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX)

    try:
        # Get fiscalization tax rules for a country
        api_response = api_instance.get_fiscalization_tax_rules(country)
        print("The response of FiscalizationApi->get_fiscalization_tax_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->get_fiscalization_tax_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166-1 alpha-2 country code (e.g., BR, PL, MX) | 

### Return type

[**FiscalizationTaxRulesResponse**](FiscalizationTaxRulesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved tax rules |  -  |
**400** | Invalid country code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fiscalization_registration**
> FiscalizationRegistrationResponse update_fiscalization_registration(x_property_id, fiscalization_registration_request)

Update fiscalization registration

Updates the fiscalization registration for the given property.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_request import FiscalizationRegistrationRequest
from cloudbeds_fiscal_document.models.fiscalization_registration_response import FiscalizationRegistrationResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | 
    fiscalization_registration_request = cloudbeds_fiscal_document.FiscalizationRegistrationRequest() # FiscalizationRegistrationRequest | 

    try:
        # Update fiscalization registration
        api_response = api_instance.update_fiscalization_registration(x_property_id, fiscalization_registration_request)
        print("The response of FiscalizationApi->update_fiscalization_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->update_fiscalization_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**|  | 
 **fiscalization_registration_request** | [**FiscalizationRegistrationRequest**](FiscalizationRegistrationRequest.md)|  | 

### Return type

[**FiscalizationRegistrationResponse**](FiscalizationRegistrationResponse.md)

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

# **update_fiscalization_tax**
> FiscalizationTaxResponse update_fiscalization_tax(x_property_id, fiscalization_tax_request)

Update fiscalization tax for a property

Creates or updates the fiscalization tax configuration for the given property

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_tax_request import FiscalizationTaxRequest
from cloudbeds_fiscal_document.models.fiscalization_tax_response import FiscalizationTaxResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    x_property_id = 56 # int | 
    fiscalization_tax_request = cloudbeds_fiscal_document.FiscalizationTaxRequest() # FiscalizationTaxRequest | 

    try:
        # Update fiscalization tax for a property
        api_response = api_instance.update_fiscalization_tax(x_property_id, fiscalization_tax_request)
        print("The response of FiscalizationApi->update_fiscalization_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->update_fiscalization_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**|  | 
 **fiscalization_tax_request** | [**FiscalizationTaxRequest**](FiscalizationTaxRequest.md)|  | 

### Return type

[**FiscalizationTaxResponse**](FiscalizationTaxResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fiscalization tax config saved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_fiscalization_data**
> FiscalizationValidationResult validate_fiscalization_data(fiscalization_registration_request)

Validate fiscalization registration data

Validates party data against country-specific fiscalization rules based on the $regime field

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_registration_request import FiscalizationRegistrationRequest
from cloudbeds_fiscal_document.models.fiscalization_validation_result import FiscalizationValidationResult
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
    api_instance = cloudbeds_fiscal_document.FiscalizationApi(api_client)
    fiscalization_registration_request = cloudbeds_fiscal_document.FiscalizationRegistrationRequest() # FiscalizationRegistrationRequest | 

    try:
        # Validate fiscalization registration data
        api_response = api_instance.validate_fiscalization_data(fiscalization_registration_request)
        print("The response of FiscalizationApi->validate_fiscalization_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalizationApi->validate_fiscalization_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fiscalization_registration_request** | [**FiscalizationRegistrationRequest**](FiscalizationRegistrationRequest.md)|  | 

### Return type

[**FiscalizationValidationResult**](FiscalizationValidationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation completed |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

