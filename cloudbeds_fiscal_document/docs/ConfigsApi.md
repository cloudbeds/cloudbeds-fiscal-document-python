# cloudbeds_fiscal_document.ConfigsApi

All URIs are relative to *http://localhost:8700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configs**](ConfigsApi.md#get_configs) | **GET** /fiscal-document/v1/configs | Get list of fiscal documents configs
[**update_configs**](ConfigsApi.md#update_configs) | **PUT** /fiscal-document/v1/configs/{documentKind} | 


# **get_configs**
> List[ConfigsResponse] get_configs(x_property_id)

Get list of fiscal documents configs

Retrieves a paginated list of fiscal documents filtered by optional criteria.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.configs_response import ConfigsResponse
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

[**List[ConfigsResponse]**](ConfigsResponse.md)

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

# **update_configs**
> ConfigsResponse update_configs(x_property_id, document_kind, configs_update_request)



Update document config.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_fiscal_document
from cloudbeds_fiscal_document.models.configs_response import ConfigsResponse
from cloudbeds_fiscal_document.models.configs_update_request import ConfigsUpdateRequest
from cloudbeds_fiscal_document.models.fiscal_document_kind import FiscalDocumentKind
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
    api_instance = cloudbeds_fiscal_document.ConfigsApi(api_client)
    x_property_id = 56 # int | Property id
    document_kind = cloudbeds_fiscal_document.FiscalDocumentKind() # FiscalDocumentKind | The kind of the fiscal document.
    configs_update_request = cloudbeds_fiscal_document.ConfigsUpdateRequest() # ConfigsUpdateRequest | 

    try:
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

