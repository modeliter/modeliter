from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class SentTaskRunEvent(BookEvent):
    sent_task_run_at: datetime
    task_run_id: str
    worker_id: str
