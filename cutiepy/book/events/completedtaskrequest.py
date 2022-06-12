from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class CompletedTaskRequest(BookEvent):
    completed_task_request_at: datetime
    task_request_id: str
