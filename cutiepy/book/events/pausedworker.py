from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class PausedWorker(BookEvent):
    paused_worker_at: datetime
    worker_id: str