# EmailSubjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The resolved subject. On the create-form variant, tokens the service cannot fill yet are left verbatim, e.g. \&quot;Grand Hotel - Invoice #[Invoice Number]\&quot;.  | 

## Example

```python
from cloudbeds_fiscal_document.models.email_subject_response import EmailSubjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSubjectResponse from a JSON string
email_subject_response_instance = EmailSubjectResponse.from_json(json)
# print the JSON string representation of the object
print(EmailSubjectResponse.to_json())

# convert the object into a dict
email_subject_response_dict = email_subject_response_instance.to_dict()
# create an instance of EmailSubjectResponse from a dict
email_subject_response_from_dict = EmailSubjectResponse.from_dict(email_subject_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


