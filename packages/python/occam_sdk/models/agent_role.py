# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AgentRole(str, Enum):
    """
    AgentRole
    """

    """
    allowed enum values
    """
    GENERAL = 'general'
    LANGUAGE_MODEL = 'language_model'
    TODO = 'todo'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentRole from a JSON string"""
        return cls(json.loads(json_str))
