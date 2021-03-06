from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class ReceivedTaskRunEvent(BookEvent):
    received_task_run_at: datetime
    task_run_id: str
    worker_id: str
    started_by_worker_at: datetime
    finished_by_worker_at: datetime
    task_result_pickle: bytes
