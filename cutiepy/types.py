from pydantic.dataclasses import dataclass
from typing import Any, TypeAlias


@dataclass
class Ok:
    value: Any


@dataclass
class Error:
    value: Exception


Result: TypeAlias = Ok | Error
