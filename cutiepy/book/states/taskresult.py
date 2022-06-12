from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from typing import Any, TypeAlias, Union

@dataclass
class TaskResultOK:
    return_value: Any

class TaskResultError(BaseModel):
    exception: Exception

    class Config:
        arbitrary_types_allowed = True

TaskResult: TypeAlias = Union[TaskResultOK, TaskResultError]
