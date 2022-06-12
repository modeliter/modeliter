from pydantic.dataclasses import dataclass
from datetime import datetime
from .workerstatus import WorkerStatus

@dataclass
class Worker:
    id: str
    status: WorkerStatus
    registered_at: datetime
    dropped_at: datetime
    sent_last_heartbeat_at: datetime
