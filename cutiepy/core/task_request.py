from pydantic.dataclasses import dataclass
from cutiepy.types import Result
from typing import Enum, Optional
from .task import Task


class TaskRequestStatus(Enum):
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"


@dataclass
class TaskRequest:
    id: str
    task: Task
    status: TaskRequestStatus
    result: Optional[Result] = None
    num_run_retries: int = 0
