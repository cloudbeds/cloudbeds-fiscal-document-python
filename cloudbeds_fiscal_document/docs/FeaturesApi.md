# cloudbeds_fiscal_document.FeaturesApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_property_features**](FeaturesApi.md#get_property_features) | **GET** /fiscal-document/v1/property/features | Get enabled features for the current user and property


# **get_property_features**
> Dict[str, bool] get_property_features(x_property_id)

Get enabled features for the current user and property

Returns a map of feature flags enabled for the authenticated user in the context of the current property.
`HAS_LEGACY_INVOICES` is true when the property holds invoices issued by MFD before it moved to fiscal
documents, whose lines and PDF still live in legacy reporting.


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
    api_instance = cloudbeds_fiscal_document.FeaturesApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        # Get enabled features for the current user and property
        api_response = api_instance.get_property_features(x_property_id)
        print("The response of FeaturesApi->get_property_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->get_property_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

**Dict[str, bool]**

### Authorization

[oauth2](../README.md#oauth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map of enabled features |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

