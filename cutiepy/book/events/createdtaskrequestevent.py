from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class CreatedTaskRequestEvent(BookEvent):
    created_task_request_at: datetime
    task_request_id: str
    function_pickle: bytes
    args_pickle: bytes
    kwargs_pickle: bytes
    max_retries_on_error: int
    max_retries_on_time_out: int
