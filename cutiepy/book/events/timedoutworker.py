from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class TimedOutWorker(BookEvent):
    timed_out_worker_at: datetime
    worker_id: str
