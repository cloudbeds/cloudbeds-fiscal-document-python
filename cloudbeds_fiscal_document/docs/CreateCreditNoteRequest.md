# CreateCreditNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_id** | **int** |  | [optional] 
**invoice_id** | **int** |  | 
**reason** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**method** | [**CreationMethod**](CreationMethod.md) |  | 
**transaction_ids** | **List[int]** | Include transactions with the specified IDs (deprecated, use &#x60;includeTransactionIds&#x60; instead) | [optional] 
**folio_ids** | **List[int]** | Include all transactions from the specified folio IDs | [optional] 
**exclude_transaction_ids** | **List[int]** | Exclude transactions with the specified IDs | [optional] 
**include_transaction_ids** | **List[int]** | Include transactions with the specified IDs | [optional] 

## Example

```python
from cloudbeds_fiscal_document.models.create_credit_note_request import CreateCreditNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteRequest from a JSON string
create_credit_note_request_instance = CreateCreditNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteRequest.to_json())

# convert the object into a dict
create_credit_note_request_dict = create_credit_note_request_instance.to_dict()
# create an instance of CreateCreditNoteRequest from a dict
create_credit_note_request_from_dict = CreateCreditNoteRequest.from_dict(create_credit_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


