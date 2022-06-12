from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class CancelledTaskRequest(BookEvent):
    cancelled_task_request_at: datetime
    task_request_id: str
