from enum import Enum

class WorkerStatus(Enum):
    AVAILABLE = "AVAILABLE"
    BUSY = "BUSY"
    DROPPED = "DROPPED"
