from datetime import datetime
from pydantic.dataclasses import dataclass
from typing import Callable
from .taskrequeststatus import TaskRequestStatus

@dataclass
class TaskRequest:
    id: str
    created_at: datetime
    function: Callable
    args: list
    kwargs: dict
    status: TaskRequestStatus
