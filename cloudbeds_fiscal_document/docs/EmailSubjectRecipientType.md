# EmailSubjectRecipientType

Which backing record a recipient id points at. Deliberately a separate schema from RecipientRequest.type even though the values match: $ref-ing that one would rename the generated RecipientRequest.TypeEnum and break every creation call site. 

## Enum

* `GUEST` (value: `'GUEST'`)

* `CONTACT` (value: `'CONTACT'`)

* `GROUP` (value: `'GROUP'`)

* `COMPANY` (value: `'COMPANY'`)

* `GROUP_PROFILE` (value: `'GROUP_PROFILE'`)

* `GROUP_PROFILE_CONTACT` (value: `'GROUP_PROFILE_CONTACT'`)

* `UNKNOWN_DEFAULT_OPEN_API` (value: `'unknown_default_open_api'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


