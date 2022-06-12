from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class TimedOutTaskRun(BookEvent):
    timed_out_task_run_at: datetime
    task_run_id: str
