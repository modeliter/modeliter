from datetime import datetime
from pydantic.dataclasses import dataclass
from .bookevent import BookEvent

@dataclass
class ReceivedHeartbeat(BookEvent):
    received_heartbeat_at: datetime
    worker_id: str
