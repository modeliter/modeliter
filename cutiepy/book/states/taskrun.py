from datetime import datetime
from pydantic.dataclasses import dataclass
from .taskrequest import TaskRequest
from .taskresult import TaskResult
from .worker import Worker

@dataclass
class TaskRun:
    id: str
    task_request_id: str
    worker_id: str
    sent_at: datetime
    started_by_worker_at: datetime
    finished_by_worker_at: datetime
    received_at: datetime
    task_result: TaskResult
