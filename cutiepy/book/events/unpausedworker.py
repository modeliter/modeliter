from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class UnpausedWorker(BookEvent):
    unpaused_worker_at: datetime
    worker_id: str
