from enum import Enum
from pydantic.dataclasses import dataclass
from datetime import datetime

class WorkerStatus(Enum):
    AVAILABLE = "AVAILABLE"
    BUSY = "BUSY"
    DROPPED = "DROPPED"

@dataclass
class Worker:
    id: str
    status: WorkerStatus
    registered_at: datetime
    dropped_at: datetime
    sent_last_heartbeat_at: datetime
