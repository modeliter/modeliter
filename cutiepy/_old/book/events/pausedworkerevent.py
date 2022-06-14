from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class PausedWorkerEvent(BookEvent):
    paused_worker_at: datetime
    worker_id: str
