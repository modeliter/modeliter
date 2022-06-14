from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class TimedOutTaskRunEvent(BookEvent):
    timed_out_task_run_at: datetime
    task_run_id: str
