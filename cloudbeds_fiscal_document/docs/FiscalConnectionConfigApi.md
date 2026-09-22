# cloudbeds_fiscal_document.FiscalConnectionConfigApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_fiscal_connection**](FiscalConnectionConfigApi.md#activate_fiscal_connection) | **POST** /fiscal-document/v1/fiscalization/connections/{connectionId}/activate | Activate a verifying connection
[**activate_fiscalization_series**](FiscalConnectionConfigApi.md#activate_fiscalization_series) | **PUT** /fiscal-document/v1/fiscalization/connections/{connectionId}/series/activate | Activate a series on a connection
[**create_fiscal_connection**](FiscalConnectionConfigApi.md#create_fiscal_connection) | **POST** /fiscal-document/v1/fiscalization/connections | Create a connection
[**deactivate_fiscalization_series**](FiscalConnectionConfigApi.md#deactivate_fiscalization_series) | **PUT** /fiscal-document/v1/fiscalization/connections/{connectionId}/series/deactivate | Deactivate a series on a connection
[**delete_connection_logo**](FiscalConnectionConfigApi.md#delete_connection_logo) | **DELETE** /fiscal-document/v1/fiscalization/connections/{connectionId}/customization/logo | Delete the branding logo for a connection
[**delete_fiscal_connection_draft**](FiscalConnectionConfigApi.md#delete_fiscal_connection_draft) | **DELETE** /fiscal-document/v1/fiscalization/connections/drafts/{providerId} | Discard a registration draft
[**disconnect_fiscal_connection**](FiscalConnectionConfigApi.md#disconnect_fiscal_connection) | **DELETE** /fiscal-document/v1/fiscalization/connections/{connectionId} | Disconnect a connection
[**get_connection_certificate**](FiscalConnectionConfigApi.md#get_connection_certificate) | **GET** /fiscal-document/v1/fiscalization/connections/{connectionId}/certificate | Get certificate status for a connection
[**get_connection_section**](FiscalConnectionConfigApi.md#get_connection_section) | **GET** /fiscal-document/v1/fiscalization/connections/{connectionId}/{sectionKey} | Get section configuration
[**get_connection_section_rules**](FiscalConnectionConfigApi.md#get_connection_section_rules) | **GET** /fiscal-document/v1/fiscalization/connections/{connectionId}/{sectionKey}/rules | Get section rules and schema
[**get_fiscal_connection**](FiscalConnectionConfigApi.md#get_fiscal_connection) | **GET** /fiscal-document/v1/fiscalization/connections/{connectionId} | Get a single connection
[**get_fiscalization_status**](FiscalConnectionConfigApi.md#get_fiscalization_status) | **GET** /fiscal-document/v1/fiscalization/status | Check if the property is ready to issue fiscal documents
[**list_fiscal_channels**](FiscalConnectionConfigApi.md#list_fiscal_channels) | **GET** /fiscal-document/v1/fiscalization/catalogue/countries/{countryCode}/channels | List fiscal channels for a country
[**list_fiscal_connection_drafts**](FiscalConnectionConfigApi.md#list_fiscal_connection_drafts) | **GET** /fiscal-document/v1/fiscalization/connections/drafts | List in-progress connection drafts
[**list_fiscal_connections**](FiscalConnectionConfigApi.md#list_fiscal_connections) | **GET** /fiscal-document/v1/fiscalization/connections | List connections for a property
[**list_fiscal_countries**](FiscalConnectionConfigApi.md#list_fiscal_countries) | **GET** /fiscal-document/v1/fiscalization/catalogue/countries | List supported countries
[**list_fiscal_document_routing**](FiscalConnectionConfigApi.md#list_fiscal_document_routing) | **GET** /fiscal-document/v1/fiscalization/routing | List all routing rules for a property
[**list_fiscal_providers**](FiscalConnectionConfigApi.md#list_fiscal_providers) | **GET** /fiscal-document/v1/fiscalization/catalogue/countries/{countryCode}/channels/{channelCode}/providers | List providers for a channel
[**patch_fiscal_document_routing**](FiscalConnectionConfigApi.md#patch_fiscal_document_routing) | **PATCH** /fiscal-document/v1/fiscalization/routing/{countryCode}/{channelCode}/{flowId} | Update a single routing rule
[**pause_fiscal_connection**](FiscalConnectionConfigApi.md#pause_fiscal_connection) | **POST** /fiscal-document/v1/fiscalization/connections/{connectionId}/pause | Pause a connection
[**replace_fiscal_document_routing**](FiscalConnectionConfigApi.md#replace_fiscal_document_routing) | **PUT** /fiscal-document/v1/fiscalization/routing | Bulk-replace routing rules
[**replace_provider_section_options**](FiscalConnectionConfigApi.md#replace_provider_section_options) | **PUT** /fiscal-document/v1/fiscalization/providers/{providerId}/{sectionKey}/options | Replace the options a provider offers for one of its sections
[**resume_fiscal_connection**](FiscalConnectionConfigApi.md#resume_fiscal_connection) | **POST** /fiscal-document/v1/fiscalization/connections/{connectionId}/resume | Resume a paused connection
[**test_fiscal_connection**](FiscalConnectionConfigApi.md#test_fiscal_connection) | **POST** /fiscal-document/v1/fiscalization/connections/{connectionId}/test | Test the connection to the tax authority
[**update_connection_section**](FiscalConnectionConfigApi.md#update_connection_section) | **PUT** /fiscal-document/v1/fiscalization/connections/{connectionId}/{sectionKey} | Update section configuration
[**update_fiscal_connection**](FiscalConnectionConfigApi.md#update_fiscal_connection) | **PUT** /fiscal-document/v1/fiscalization/connections/{connectionId} | Update a connection
[**upload_connection_certificate**](FiscalConnectionConfigApi.md#upload_connection_certificate) | **POST** /fiscal-document/v1/fiscalization/connections/{connectionId}/certificate | Upload a certificate for a connection
[**upload_connection_logo**](FiscalConnectionConfigApi.md#upload_connection_logo) | **POST** /fiscal-document/v1/fiscalization/connections/{connectionId}/customization/logo | Upload the branding logo for a connection
[**upsert_fiscal_connection_draft**](FiscalConnectionConfigApi.md#upsert_fiscal_connection_draft) | **PUT** /fiscal-document/v1/fiscalization/connections/drafts/{providerId} | Upsert a registration draft


# **activate_fiscal_connection**
> FiscalConnection activate_fiscal_connection(x_property_id, connection_id, fiscal_connection_activate_request=fiscal_connection_activate_request)

Activate a verifying connection

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
from cloudbeds_fiscal_document.models.fiscal_connection_activate_request import FiscalConnectionActivateRequest
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    fiscal_connection_activate_request = cloudbeds_fiscal_document.FiscalConnectionActivateRequest() # FiscalConnectionActivateRequest |  (optional)

    try:
        # Activate a verifying connection
        api_response = api_instance.activate_fiscal_connection(x_property_id, connection_id, fiscal_connection_activate_request=fiscal_connection_activate_request)
        print("The response of FiscalConnectionConfigApi->activate_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->activate_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **fiscal_connection_activate_request** | [**FiscalConnectionActivateRequest**](FiscalConnectionActivateRequest.md)|  | [optional] 

### Return type

[**FiscalConnection**](FiscalConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_fiscalization_series**
> FiscalizationSeriesResponse activate_fiscalization_series(x_property_id, connection_id, activate_series_request)

Activate a series on a connection

Activates the given series and deactivates the connection's other series of the same document kind.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.activate_series_request import ActivateSeriesRequest
from cloudbeds_fiscal_document.models.fiscalization_series_response import FiscalizationSeriesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    activate_series_request = cloudbeds_fiscal_document.ActivateSeriesRequest() # ActivateSeriesRequest | 

    try:
        # Activate a series on a connection
        api_response = api_instance.activate_fiscalization_series(x_property_id, connection_id, activate_series_request)
        print("The response of FiscalConnectionConfigApi->activate_fiscalization_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->activate_fiscalization_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **activate_series_request** | [**ActivateSeriesRequest**](ActivateSeriesRequest.md)|  | 

### Return type

[**FiscalizationSeriesResponse**](FiscalizationSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fiscal_connection**
> FiscalConnection create_fiscal_connection(x_property_id, fiscal_connection_create_request)

Create a connection

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
from cloudbeds_fiscal_document.models.fiscal_connection_create_request import FiscalConnectionCreateRequest
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    fiscal_connection_create_request = cloudbeds_fiscal_document.FiscalConnectionCreateRequest() # FiscalConnectionCreateRequest | 

    try:
        # Create a connection
        api_response = api_instance.create_fiscal_connection(x_property_id, fiscal_connection_create_request)
        print("The response of FiscalConnectionConfigApi->create_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->create_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **fiscal_connection_create_request** | [**FiscalConnectionCreateRequest**](FiscalConnectionCreateRequest.md)|  | 

### Return type

[**FiscalConnection**](FiscalConnection.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Provider already connected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_fiscalization_series**
> FiscalizationSeriesResponse deactivate_fiscalization_series(x_property_id, connection_id, activate_series_request)

Deactivate a series on a connection

Deactivates the given series. A document kind left with no active series will fail to issue documents until another series is activated.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.activate_series_request import ActivateSeriesRequest
from cloudbeds_fiscal_document.models.fiscalization_series_response import FiscalizationSeriesResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    activate_series_request = cloudbeds_fiscal_document.ActivateSeriesRequest() # ActivateSeriesRequest | 

    try:
        # Deactivate a series on a connection
        api_response = api_instance.deactivate_fiscalization_series(x_property_id, connection_id, activate_series_request)
        print("The response of FiscalConnectionConfigApi->deactivate_fiscalization_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->deactivate_fiscalization_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **activate_series_request** | [**ActivateSeriesRequest**](ActivateSeriesRequest.md)|  | 

### Return type

[**FiscalizationSeriesResponse**](FiscalizationSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_logo**
> delete_connection_logo(x_property_id, connection_id)

Delete the branding logo for a connection

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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Delete the branding logo for a connection
        api_instance.delete_connection_logo(x_property_id, connection_id)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->delete_connection_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Logo deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fiscal_connection_draft**
> delete_fiscal_connection_draft(x_property_id, provider_id)

Discard a registration draft

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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    provider_id = 'provider_id_example' # str | 

    try:
        # Discard a registration draft
        api_instance.delete_fiscal_connection_draft(x_property_id, provider_id)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->delete_fiscal_connection_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **provider_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_fiscal_connection**
> disconnect_fiscal_connection(x_property_id, connection_id)

Disconnect a connection

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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Disconnect a connection
        api_instance.disconnect_fiscal_connection(x_property_id, connection_id)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->disconnect_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Disconnected |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_certificate**
> FiscalizationCertificateStatus get_connection_certificate(x_property_id, connection_id)

Get certificate status for a connection

Returns metadata about the stored fiscalization certificate for the given connection,
including expiry date and live provider validity. Returns 404 if no certificate has
been uploaded for this connection or if the provider does not require a certificate.
The provider validity check is best-effort: on provider unavailability the stored
status is returned without failing the request.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_certificate_status import FiscalizationCertificateStatus
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Get certificate status for a connection
        api_response = api_instance.get_connection_certificate(x_property_id, connection_id)
        print("The response of FiscalConnectionConfigApi->get_connection_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->get_connection_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

[**FiscalizationCertificateStatus**](FiscalizationCertificateStatus.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate metadata retrieved successfully |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_section**
> Dict[str, object] get_connection_section(x_property_id, connection_id, section_key)

Get section configuration

Returns the current configuration for the given section, reading from the same data sources as the legacy endpoints.

### Example

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    section_key = 'section_key_example' # str | Section key: registration, certificate, externalAuthorization, authentication, series, taxCodes, paymentMethods, items, operators, customization

    try:
        # Get section configuration
        api_response = api_instance.get_connection_section(x_property_id, connection_id, section_key)
        print("The response of FiscalConnectionConfigApi->get_connection_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->get_connection_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **section_key** | **str**| Section key: registration, certificate, externalAuthorization, authentication, series, taxCodes, paymentMethods, items, operators, customization | 

### Return type

**Dict[str, object]**

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

# **get_connection_section_rules**
> Dict[str, object] get_connection_section_rules(x_property_id, connection_id, section_key)

Get section rules and schema

Returns available options and field definitions for sections that have rules (series, taxCodes, paymentMethods, items, operators). Returns 404 for sections without rules.

### Example

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_fiscal_document.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_fiscal_document.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    section_key = 'section_key_example' # str | 

    try:
        # Get section rules and schema
        api_response = api_instance.get_connection_section_rules(x_property_id, connection_id, section_key)
        print("The response of FiscalConnectionConfigApi->get_connection_section_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->get_connection_section_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **section_key** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_fiscal_connection**
> FiscalConnection get_fiscal_connection(x_property_id, connection_id)

Get a single connection

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Get a single connection
        api_response = api_instance.get_fiscal_connection(x_property_id, connection_id)
        print("The response of FiscalConnectionConfigApi->get_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->get_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

[**FiscalConnection**](FiscalConnection.md)

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

# **get_fiscalization_status**
> FiscalizationStatusResponse get_fiscalization_status(x_property_id)

Check if the property is ready to issue fiscal documents

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscalization_status_response import FiscalizationStatusResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # Check if the property is ready to issue fiscal documents
        api_response = api_instance.get_fiscalization_status(x_property_id)
        print("The response of FiscalConnectionConfigApi->get_fiscalization_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->get_fiscalization_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**FiscalizationStatusResponse**](FiscalizationStatusResponse.md)

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

# **list_fiscal_channels**
> FiscalChannelListResponse list_fiscal_channels(country_code)

List fiscal channels for a country

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_channel_list_response import FiscalChannelListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    country_code = 'country_code_example' # str | 

    try:
        # List fiscal channels for a country
        api_response = api_instance.list_fiscal_channels(country_code)
        print("The response of FiscalConnectionConfigApi->list_fiscal_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->list_fiscal_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**|  | 

### Return type

[**FiscalChannelListResponse**](FiscalChannelListResponse.md)

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

# **list_fiscal_connection_drafts**
> FiscalConnectionDraftListResponse list_fiscal_connection_drafts(x_property_id)

List in-progress connection drafts

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection_draft_list_response import FiscalConnectionDraftListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # List in-progress connection drafts
        api_response = api_instance.list_fiscal_connection_drafts(x_property_id)
        print("The response of FiscalConnectionConfigApi->list_fiscal_connection_drafts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->list_fiscal_connection_drafts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**FiscalConnectionDraftListResponse**](FiscalConnectionDraftListResponse.md)

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

# **list_fiscal_connections**
> FiscalConnectionListResponse list_fiscal_connections(x_property_id, drafts=drafts)

List connections for a property

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection_list_response import FiscalConnectionListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    drafts = False # bool |  (optional) (default to False)

    try:
        # List connections for a property
        api_response = api_instance.list_fiscal_connections(x_property_id, drafts=drafts)
        print("The response of FiscalConnectionConfigApi->list_fiscal_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->list_fiscal_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **drafts** | **bool**|  | [optional] [default to False]

### Return type

[**FiscalConnectionListResponse**](FiscalConnectionListResponse.md)

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

# **list_fiscal_countries**
> FiscalCountryListResponse list_fiscal_countries()

List supported countries

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_country_list_response import FiscalCountryListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)

    try:
        # List supported countries
        api_response = api_instance.list_fiscal_countries()
        print("The response of FiscalConnectionConfigApi->list_fiscal_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->list_fiscal_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FiscalCountryListResponse**](FiscalCountryListResponse.md)

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

# **list_fiscal_document_routing**
> FiscalRoutingListResponse list_fiscal_document_routing(x_property_id)

List all routing rules for a property

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_routing_list_response import FiscalRoutingListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # List all routing rules for a property
        api_response = api_instance.list_fiscal_document_routing(x_property_id)
        print("The response of FiscalConnectionConfigApi->list_fiscal_document_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->list_fiscal_document_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**FiscalRoutingListResponse**](FiscalRoutingListResponse.md)

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

# **list_fiscal_providers**
> FiscalProviderListResponse list_fiscal_providers(country_code, channel_code, enabled=enabled)

List providers for a channel

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_provider_list_response import FiscalProviderListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    country_code = 'country_code_example' # str | 
    channel_code = 'channel_code_example' # str | 
    enabled = False # bool |  (optional) (default to False)

    try:
        # List providers for a channel
        api_response = api_instance.list_fiscal_providers(country_code, channel_code, enabled=enabled)
        print("The response of FiscalConnectionConfigApi->list_fiscal_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->list_fiscal_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**|  | 
 **channel_code** | **str**|  | 
 **enabled** | **bool**|  | [optional] [default to False]

### Return type

[**FiscalProviderListResponse**](FiscalProviderListResponse.md)

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

# **patch_fiscal_document_routing**
> FiscalRoutingRule patch_fiscal_document_routing(x_property_id, country_code, channel_code, flow_id, fiscal_routing_rule_patch)

Update a single routing rule

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_routing_rule import FiscalRoutingRule
from cloudbeds_fiscal_document.models.fiscal_routing_rule_patch import FiscalRoutingRulePatch
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    country_code = 'country_code_example' # str | 
    channel_code = 'channel_code_example' # str | 
    flow_id = 'flow_id_example' # str | 
    fiscal_routing_rule_patch = cloudbeds_fiscal_document.FiscalRoutingRulePatch() # FiscalRoutingRulePatch | 

    try:
        # Update a single routing rule
        api_response = api_instance.patch_fiscal_document_routing(x_property_id, country_code, channel_code, flow_id, fiscal_routing_rule_patch)
        print("The response of FiscalConnectionConfigApi->patch_fiscal_document_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->patch_fiscal_document_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **country_code** | **str**|  | 
 **channel_code** | **str**|  | 
 **flow_id** | **str**|  | 
 **fiscal_routing_rule_patch** | [**FiscalRoutingRulePatch**](FiscalRoutingRulePatch.md)|  | 

### Return type

[**FiscalRoutingRule**](FiscalRoutingRule.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_fiscal_connection**
> FiscalConnection pause_fiscal_connection(x_property_id, connection_id)

Pause a connection

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Pause a connection
        api_response = api_instance.pause_fiscal_connection(x_property_id, connection_id)
        print("The response of FiscalConnectionConfigApi->pause_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->pause_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

[**FiscalConnection**](FiscalConnection.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_fiscal_document_routing**
> FiscalRoutingListResponse replace_fiscal_document_routing(x_property_id, fiscal_routing_list_response)

Bulk-replace routing rules

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_routing_list_response import FiscalRoutingListResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    fiscal_routing_list_response = cloudbeds_fiscal_document.FiscalRoutingListResponse() # FiscalRoutingListResponse | 

    try:
        # Bulk-replace routing rules
        api_response = api_instance.replace_fiscal_document_routing(x_property_id, fiscal_routing_list_response)
        print("The response of FiscalConnectionConfigApi->replace_fiscal_document_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->replace_fiscal_document_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **fiscal_routing_list_response** | [**FiscalRoutingListResponse**](FiscalRoutingListResponse.md)|  | 

### Return type

[**FiscalRoutingListResponse**](FiscalRoutingListResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_provider_section_options**
> ProviderOptionsReplaceResponse replace_provider_section_options(x_property_id, provider_id, section_key, provider_options_replace_request)

Replace the options a provider offers for one of its sections

Partner-facing. Replaces the selectable options this provider offers in one scope, so a hotelier can map Cloudbeds data onto the partner's own values in the Cloudbeds UI. Omit connectionId for a catalogue that is the same for every property; send it when the values differ per customer account. Values dropped from a later push are deactivated, not deleted, so mappings already made against them keep their label. Restricted to the OAuth client registered for the provider. X-PROPERTY-ID is required even for a provider-wide push and must identify a property covered by the token's consent. A supplied connectionId must belong to this provider and a property covered by the token's resources claim.


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.provider_options_replace_request import ProviderOptionsReplaceRequest
from cloudbeds_fiscal_document.models.provider_options_replace_response import ProviderOptionsReplaceResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    provider_id = 'provider_id_example' # str | 
    section_key = 'section_key_example' # str | Section key: taxCodes, paymentMethods, items, operators, series
    provider_options_replace_request = cloudbeds_fiscal_document.ProviderOptionsReplaceRequest() # ProviderOptionsReplaceRequest | 

    try:
        # Replace the options a provider offers for one of its sections
        api_response = api_instance.replace_provider_section_options(x_property_id, provider_id, section_key, provider_options_replace_request)
        print("The response of FiscalConnectionConfigApi->replace_provider_section_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->replace_provider_section_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **provider_id** | **str**|  | 
 **section_key** | **str**| Section key: taxCodes, paymentMethods, items, operators, series | 
 **provider_options_replace_request** | [**ProviderOptionsReplaceRequest**](ProviderOptionsReplaceRequest.md)|  | 

### Return type

[**ProviderOptionsReplaceResponse**](ProviderOptionsReplaceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_fiscal_connection**
> FiscalConnection resume_fiscal_connection(x_property_id, connection_id)

Resume a paused connection

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Resume a paused connection
        api_response = api_instance.resume_fiscal_connection(x_property_id, connection_id)
        print("The response of FiscalConnectionConfigApi->resume_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->resume_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

[**FiscalConnection**](FiscalConnection.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_fiscal_connection**
> FiscalConnectionTestResult test_fiscal_connection(x_property_id, connection_id)

Test the connection to the tax authority

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection_test_result import FiscalConnectionTestResult
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 

    try:
        # Test the connection to the tax authority
        api_response = api_instance.test_fiscal_connection(x_property_id, connection_id)
        print("The response of FiscalConnectionConfigApi->test_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->test_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 

### Return type

[**FiscalConnectionTestResult**](FiscalConnectionTestResult.md)

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

# **update_connection_section**
> FiscalConnection update_connection_section(x_property_id, connection_id, section_key, request_body)

Update section configuration

Updates the configuration for the given section. Calls the provider API when applicable (registration, certificate, authentication, series). Auto-activates the connection when all required sections are complete.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    section_key = 'section_key_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update section configuration
        api_response = api_instance.update_connection_section(x_property_id, connection_id, section_key, request_body)
        print("The response of FiscalConnectionConfigApi->update_connection_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->update_connection_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **section_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**FiscalConnection**](FiscalConnection.md)

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

# **update_fiscal_connection**
> FiscalConnection update_fiscal_connection(x_property_id, connection_id, fiscal_connection_update_request)

Update a connection

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection import FiscalConnection
from cloudbeds_fiscal_document.models.fiscal_connection_update_request import FiscalConnectionUpdateRequest
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    fiscal_connection_update_request = cloudbeds_fiscal_document.FiscalConnectionUpdateRequest() # FiscalConnectionUpdateRequest | 

    try:
        # Update a connection
        api_response = api_instance.update_fiscal_connection(x_property_id, connection_id, fiscal_connection_update_request)
        print("The response of FiscalConnectionConfigApi->update_fiscal_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->update_fiscal_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **fiscal_connection_update_request** | [**FiscalConnectionUpdateRequest**](FiscalConnectionUpdateRequest.md)|  | 

### Return type

[**FiscalConnection**](FiscalConnection.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_connection_certificate**
> upload_connection_certificate(x_property_id, connection_id, file, private_key=private_key, password=password)

Upload a certificate for a connection

Uploads a certificate file for the given connection's fiscalization provider.
Resolves the provider and country from the connectionId. Mirrors the deprecated
singular endpoint contract but is scoped by connectionId.


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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    file = None # bytearray | Certificate or ownership document file
    private_key = None # bytearray | Private key file (required for MX e.firma) (optional)
    password = 'password_example' # str | Certificate or private key password (if required) (optional)

    try:
        # Upload a certificate for a connection
        api_instance.upload_connection_certificate(x_property_id, connection_id, file, private_key=private_key, password=password)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->upload_connection_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **file** | **bytearray**| Certificate or ownership document file | 
 **private_key** | **bytearray**| Private key file (required for MX e.firma) | [optional] 
 **password** | **str**| Certificate or private key password (if required) | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Certificate uploaded and submitted for verification |  -  |
**400** | Bad Request |  -  |
**422** | Invalid certificate (rejected by provider) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_connection_logo**
> GetLogoResponse upload_connection_logo(x_property_id, connection_id, file)

Upload the branding logo for a connection

Uploads the logo the fiscalization provider renders on this connection's documents. This is
not the document-config logo behind /configs/logo, which feeds the locally rendered PDF
templates from a different S3 path.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.get_logo_response import GetLogoResponse
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    connection_id = 56 # int | 
    file = None # bytearray | Logo image file, PNG or JPEG

    try:
        # Upload the branding logo for a connection
        api_response = api_instance.upload_connection_logo(x_property_id, connection_id, file)
        print("The response of FiscalConnectionConfigApi->upload_connection_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->upload_connection_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **connection_id** | **int**|  | 
 **file** | **bytearray**| Logo image file, PNG or JPEG | 

### Return type

[**GetLogoResponse**](GetLogoResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logo uploaded successfully |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_fiscal_connection_draft**
> FiscalConnectionDraft upsert_fiscal_connection_draft(x_property_id, provider_id, fiscal_connection_draft_upsert_request)

Upsert a registration draft

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.fiscal_connection_draft import FiscalConnectionDraft
from cloudbeds_fiscal_document.models.fiscal_connection_draft_upsert_request import FiscalConnectionDraftUpsertRequest
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
    api_instance = cloudbeds_fiscal_document.FiscalConnectionConfigApi(api_client)
    x_property_id = 56 # int | Property id
    provider_id = 'provider_id_example' # str | 
    fiscal_connection_draft_upsert_request = cloudbeds_fiscal_document.FiscalConnectionDraftUpsertRequest() # FiscalConnectionDraftUpsertRequest | 

    try:
        # Upsert a registration draft
        api_response = api_instance.upsert_fiscal_connection_draft(x_property_id, provider_id, fiscal_connection_draft_upsert_request)
        print("The response of FiscalConnectionConfigApi->upsert_fiscal_connection_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalConnectionConfigApi->upsert_fiscal_connection_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **provider_id** | **str**|  | 
 **fiscal_connection_draft_upsert_request** | [**FiscalConnectionDraftUpsertRequest**](FiscalConnectionDraftUpsertRequest.md)|  | 

### Return type

[**FiscalConnectionDraft**](FiscalConnectionDraft.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

