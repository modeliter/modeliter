from cutiepy.types import Result
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import Any, Optional
from cutiepy.tasks import Task


class TaskRequestStatus(Enum):
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"


@dataclass
class TaskRequest:
    id: str
    task: Task
    args: list
    kwargs: dict[str, Any]
    status: Optional[TaskRequestStatus] = None
    result: Optional[Result] = None
    num_run_retries: int = 0
