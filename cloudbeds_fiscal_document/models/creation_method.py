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


class CreationMethod(str, Enum):
    """
    CreationMethod
    """

    """
    allowed enum values
    """
    VOID = 'VOID'
    ADJUSTMENT = 'ADJUSTMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CreationMethod from a JSON string"""
        return cls(json.loads(json_str))


