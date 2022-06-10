from cutiepy.types import Result
from enum import Enum
from pydantic.dataclasses import dataclass, Field
from typing import Any, Dict, List, Optional
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
    task_args: List[Any] = Field(default_factory=list)
    task_kwargs: Dict[str, Any] = Field(default_factory=dict)
    status: Optional[TaskRequestStatus] = None
    result: Optional[Result] = None
    num_run_retries: int = 0
