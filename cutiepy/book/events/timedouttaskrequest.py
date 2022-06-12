from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class TimedOutTaskRequest(BookEvent):
    timed_out_task_request_at: datetime
    task_request_id: str
