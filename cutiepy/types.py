from pydantic.dataclasses import dataclass
from typing import Any, Dict, TypeAlias


@dataclass
class Ok:
    value: Any


@dataclass
class Error:
    value: Any


Result: TypeAlias = Ok | Error
TagKey: TypeAlias = str
TagValue: TypeAlias = int | str
Tags: TypeAlias = Dict[TagKey, TagValue]
