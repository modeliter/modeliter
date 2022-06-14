from datetime import datetime
from pydantic.dataclasses import dataclass
from cutiepy.book.events.bookevent import BookEvent

@dataclass
class ReceivedHeartbeatEvent(BookEvent):
    received_heartbeat_at: datetime
    worker_id: str
