from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cutiepy.core import Task
    from cutiepy.types import Result
    from datetime import datetime
    from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class TaskRun:
    id: str
    task: Task
    broker_ref: str
    worker_ref: str
    broker_created_at: datetime
    worker_received_at: Optional[datetime]
    worker_returned_at: Optional[datetime]
    broker_received_at: Optional[datetime]
    result: Result
