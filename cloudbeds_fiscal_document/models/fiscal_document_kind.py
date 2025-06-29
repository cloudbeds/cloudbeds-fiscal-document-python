# coding: utf-8

"""
    Fiscal document service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FiscalDocumentKind(str, Enum):
    """
    Kind of fiscal document
    """

    """
    allowed enum values
    """
    INVOICE = 'INVOICE'
    CREDIT_NOTE = 'CREDIT_NOTE'
    RECEIPT = 'RECEIPT'
    RECTIFY_INVOICE = 'RECTIFY_INVOICE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FiscalDocumentKind from a JSON string"""
        return cls(json.loads(json_str))


