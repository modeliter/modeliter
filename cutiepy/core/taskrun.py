from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cutiepy.core import Task
    from cutiepy.types import Result
    from datetime import datetime
from pydantic.dataclasses import dataclass


@dataclass
class TaskRun:
    id: str
    task: Task
    broker_ref: str
    worker_ref: str
    broker_sent_at: datetime
    broker_received_at: datetime
    worker_started_at: datetime
    worker_finished_at: datetime
    result: Result
