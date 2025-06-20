# coding: utf-8

"""
    Fiscal document service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ConfigsUpdateRequest(BaseModel):
    """
    ConfigsUpdateRequest
    """ # noqa: E501
    show_detailed_tax_fee: StrictBool = Field(alias="showDetailedTaxFee")
    charge_breakdown: StrictBool = Field(alias="chargeBreakdown")
    use_guest_lang: StrictBool = Field(alias="useGuestLang")
    due_days: Optional[StrictInt] = Field(default=None, alias="dueDays")
    lang: Optional[StrictStr] = None
    prefix: Optional[StrictStr] = None
    suffix: Optional[StrictStr] = None
    legal_company_name: Optional[StrictStr] = Field(default=None, alias="legalCompanyName")
    title: Optional[Dict[str, StrictStr]] = None
    show_legal_company_name: StrictBool = Field(alias="showLegalCompanyName")
    include_room_number: StrictBool = Field(alias="includeRoomNumber")
    use_document_number: StrictBool = Field(alias="useDocumentNumber")
    is_compact: StrictBool = Field(alias="isCompact")
    tax_id1: Optional[StrictStr] = Field(default=None, alias="taxId1")
    tax_id2: Optional[StrictStr] = Field(default=None, alias="taxId2")
    cpf: Optional[StrictStr] = None
    custom_text: Optional[Dict[str, StrictStr]] = Field(default=None, alias="customText")
    __properties: ClassVar[List[str]] = ["showDetailedTaxFee", "chargeBreakdown", "useGuestLang", "dueDays", "lang", "prefix", "suffix", "legalCompanyName", "title", "showLegalCompanyName", "includeRoomNumber", "useDocumentNumber", "isCompact", "taxId1", "taxId2", "cpf", "customText"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConfigsUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if due_days (nullable) is None
        # and model_fields_set contains the field
        if self.due_days is None and "due_days" in self.model_fields_set:
            _dict['dueDays'] = None

        # set to None if lang (nullable) is None
        # and model_fields_set contains the field
        if self.lang is None and "lang" in self.model_fields_set:
            _dict['lang'] = None

        # set to None if prefix (nullable) is None
        # and model_fields_set contains the field
        if self.prefix is None and "prefix" in self.model_fields_set:
            _dict['prefix'] = None

        # set to None if suffix (nullable) is None
        # and model_fields_set contains the field
        if self.suffix is None and "suffix" in self.model_fields_set:
            _dict['suffix'] = None

        # set to None if legal_company_name (nullable) is None
        # and model_fields_set contains the field
        if self.legal_company_name is None and "legal_company_name" in self.model_fields_set:
            _dict['legalCompanyName'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if tax_id1 (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id1 is None and "tax_id1" in self.model_fields_set:
            _dict['taxId1'] = None

        # set to None if tax_id2 (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id2 is None and "tax_id2" in self.model_fields_set:
            _dict['taxId2'] = None

        # set to None if cpf (nullable) is None
        # and model_fields_set contains the field
        if self.cpf is None and "cpf" in self.model_fields_set:
            _dict['cpf'] = None

        # set to None if custom_text (nullable) is None
        # and model_fields_set contains the field
        if self.custom_text is None and "custom_text" in self.model_fields_set:
            _dict['customText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigsUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "showDetailedTaxFee": obj.get("showDetailedTaxFee"),
            "chargeBreakdown": obj.get("chargeBreakdown"),
            "useGuestLang": obj.get("useGuestLang"),
            "dueDays": obj.get("dueDays"),
            "lang": obj.get("lang"),
            "prefix": obj.get("prefix"),
            "suffix": obj.get("suffix"),
            "legalCompanyName": obj.get("legalCompanyName"),
            "title": obj.get("title"),
            "showLegalCompanyName": obj.get("showLegalCompanyName"),
            "includeRoomNumber": obj.get("includeRoomNumber"),
            "useDocumentNumber": obj.get("useDocumentNumber"),
            "isCompact": obj.get("isCompact"),
            "taxId1": obj.get("taxId1"),
            "taxId2": obj.get("taxId2"),
            "cpf": obj.get("cpf"),
            "customText": obj.get("customText")
        })
        return _obj


