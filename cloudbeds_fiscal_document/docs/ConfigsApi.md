# cloudbeds_fiscal_document.ConfigsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crop_logo**](ConfigsApi.md#crop_logo) | **PATCH** /fiscal-document/v1/configs/logo | Crop logo image for fiscal documents
[**delete_logo**](ConfigsApi.md#delete_logo) | **DELETE** /fiscal-document/v1/configs/logo | Delete logo image for fiscal documents
[**get_configs**](ConfigsApi.md#get_configs) | **GET** /fiscal-document/v1/configs | Get list of fiscal documents configs
[**get_logo**](ConfigsApi.md#get_logo) | **GET** /fiscal-document/v1/configs/logo | Get logo image for fiscal documents
[**get_pdf_preview**](ConfigsApi.md#get_pdf_preview) | **GET** /fiscal-document/v1/configs/preview | Get PDF document preview
[**get_property_settings**](ConfigsApi.md#get_property_settings) | **GET** /fiscal-document/v1/configs/property-settings | Get property-level document settings
[**update_configs**](ConfigsApi.md#update_configs) | **PUT** /fiscal-document/v1/configs/{documentKind} | Updates a config of a specific kind
[**update_property_settings**](ConfigsApi.md#update_property_settings) | **PATCH** /fiscal-document/v1/configs/property-settings | Update property-level document settings
[**upload_logo**](ConfigsApi.md#upload_logo) | **POST** /fiscal-document/v1/configs/logo | Upload logo image for fiscal documents


# **crop_logo**
> crop_logo(x_property_id, crop_logo_request)

Crop logo image for fiscal documents

Crop the previously uploaded logo. The original is preserved so subsequent crops always start from the full original image. Output is stored as PNG and resized to at most 1000 px on the longest dimension.


### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.crop_logo_request import CropLogoRequest
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id
    crop_logo_request = cloudbeds_fiscal_document.CropLogoRequest() # CropLogoRequest | 

    try:
        # Crop logo image for fiscal documents
        api_instance.crop_logo(x_property_id, crop_logo_request)
    except Exception as e:
        print("Exception when calling ConfigsApi->crop_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **crop_logo_request** | [**CropLogoRequest**](CropLogoRequest.md)|  | 

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
**200** | Logo cropped successfully |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logo**
> delete_logo(x_property_id)

Delete logo image for fiscal documents

Delete the logo image used in fiscal document templates.

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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # Delete logo image for fiscal documents
        api_instance.delete_logo(x_property_id)
    except Exception as e:
        print("Exception when calling ConfigsApi->delete_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

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
**200** | Logo deleted successfully |  -  |
**404** | Not found |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configs**
> PropertyConfigsResponse get_configs(x_property_id)

Get list of fiscal documents configs

Retrieves a paginated list of fiscal documents filtered by optional criteria.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.property_configs_response import PropertyConfigsResponse
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # Get list of fiscal documents configs
        api_response = api_instance.get_configs(x_property_id)
        print("The response of ConfigsApi->get_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**PropertyConfigsResponse**](PropertyConfigsResponse.md)

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

# **get_logo**
> GetLogoResponse get_logo(x_property_id)

Get logo image for fiscal documents

Retrieve the logo image used in fiscal document templates as a presigned URL.

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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # Get logo image for fiscal documents
        api_response = api_instance.get_logo(x_property_id)
        print("The response of ConfigsApi->get_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**GetLogoResponse**](GetLogoResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logo URL retrieved successfully |  -  |
**404** | Not found |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_preview**
> bytearray get_pdf_preview(x_property_id, preview_request=preview_request)

Get PDF document preview

Build and return PDF document

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.preview_request import PreviewRequest
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id
    preview_request = cloudbeds_fiscal_document.PreviewRequest() # PreviewRequest |  (optional)

    try:
        # Get PDF document preview
        api_response = api_instance.get_pdf_preview(x_property_id, preview_request=preview_request)
        print("The response of ConfigsApi->get_pdf_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_pdf_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **preview_request** | [**PreviewRequest**](.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_settings**
> PropertySettingsResponse get_property_settings(x_property_id)

Get property-level document settings

Registry facts printed under the issuer on fiscal documents (e.g. Spain's tourism classification and registry code). Property-level, shared by every document kind.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.property_settings_response import PropertySettingsResponse
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # Get property-level document settings
        api_response = api_instance.get_property_settings(x_property_id)
        print("The response of ConfigsApi->get_property_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_property_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**PropertySettingsResponse**](PropertySettingsResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configs**
> ConfigsResponse update_configs(x_property_id, document_kind, configs_update_request)

Updates a config of a specific kind

Update document config.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.configs_response import ConfigsResponse
from cloudbeds_fiscal_document.models.configs_update_request import ConfigsUpdateRequest
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | The kind of the fiscal document.
    configs_update_request = cloudbeds_fiscal_document.ConfigsUpdateRequest() # ConfigsUpdateRequest | 

    try:
        # Updates a config of a specific kind
        api_response = api_instance.update_configs(x_property_id, document_kind, configs_update_request)
        print("The response of ConfigsApi->update_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->update_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **document_kind** | [**FiscalDocumentKind**](.md)| The kind of the fiscal document. | 
 **configs_update_request** | [**ConfigsUpdateRequest**](ConfigsUpdateRequest.md)|  | 

### Return type

[**ConfigsResponse**](ConfigsResponse.md)

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

# **update_property_settings**
> PropertySettingsResponse update_property_settings(x_property_id, property_settings_update_request)

Update property-level document settings

A concern object that is present replaces that concern as a whole (blank strings are stored as null); a concern that is absent is left untouched.

### Example

* OAuth Authentication (oauth2):
* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.property_settings_response import PropertySettingsResponse
from cloudbeds_fiscal_document.models.property_settings_update_request import PropertySettingsUpdateRequest
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id
    property_settings_update_request = cloudbeds_fiscal_document.PropertySettingsUpdateRequest() # PropertySettingsUpdateRequest | 

    try:
        # Update property-level document settings
        api_response = api_instance.update_property_settings(x_property_id, property_settings_update_request)
        print("The response of ConfigsApi->update_property_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->update_property_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **property_settings_update_request** | [**PropertySettingsUpdateRequest**](PropertySettingsUpdateRequest.md)|  | 

### Return type

[**PropertySettingsResponse**](PropertySettingsResponse.md)

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
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_logo**
> upload_logo(x_property_id, file)

Upload logo image for fiscal documents

Upload a logo image to be used in fiscal document templates.

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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id
    file = None # bytearray | Logo image file

    try:
        # Upload logo image for fiscal documents
        api_instance.upload_logo(x_property_id, file)
    except Exception as e:
        print("Exception when calling ConfigsApi->upload_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **file** | **bytearray**| Logo image file | 

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
**200** | Logo uploaded successfully |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

