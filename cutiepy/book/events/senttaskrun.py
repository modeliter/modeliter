from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class SentTaskRun(BookEvent):
    sent_task_run_at: datetime
    task_run_id: str
    worker_id: str
