from cutiepy.taskrequests import TaskRequest
from cutiepy.types import Result
from datetime import datetime
from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class TaskRun:
    id: str
    task_request: TaskRequest
    worker_ref: str
    broker_created_at: datetime
    worker_received_at: Optional[datetime]
    worker_returned_at: Optional[datetime]
    broker_received_at: Optional[datetime]
    result: Result
