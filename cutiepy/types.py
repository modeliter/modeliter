from pydantic.dataclasses import dataclass
from typing import Any, Dict, TypeAlias


@dataclass
class Ok:
    value: Any


@dataclass
class Error:
    value: Exception


Result: TypeAlias = Ok | Error
TagKey: TypeAlias = str
TagValue: TypeAlias = int | str
Tag: TypeAlias = Dict[TagKey, TagValue]
