from datetime import datetime
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import Callable

class TaskRequestStatus(Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    TIMED_OUT = "TIMED_OUT"
    CANCELLED = "CANCELLED"

@dataclass
class TaskRequest:
    id: str
    created_at: datetime
    function: Callable
    args: list
    kwargs: dict
    status: TaskRequestStatus
