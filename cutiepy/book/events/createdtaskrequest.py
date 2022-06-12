from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class CreatedTaskRequest(BookEvent):
    created_task_request_at: datetime
    task_request_id: str
    function_pickle: bytes
    args_pickle: bytes
    kwargs_pickle: bytes
    max_retries_on_time_out: int
    max_retries_on_error: int
