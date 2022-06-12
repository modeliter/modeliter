from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class TimedOutTaskRequestEvent(BookEvent):
    timed_out_task_request_at: datetime
    task_request_id: str
