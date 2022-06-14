from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class UnpausedWorkerEvent(BookEvent):
    unpaused_worker_at: datetime
    worker_id: str
