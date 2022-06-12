from cutiepy.duckdb import DuckDBSchema, DuckDBTable
from pydantic.dataclasses import dataclass
from .cancelledtaskrequesttable import CancelledTaskRequestTable
from .completedtaskrequesttable import CompletedTaskRequestTable
from .createdtaskrequesttable import CreatedTaskRequestTable
from .pausedworkertable import PausedWorkerTable
from .receivedheartbeattable import ReceivedHeartbeatTable
from .receivedtaskruntable import ReceivedTaskRunTable
from .registeredworkertable import RegisteredWorkerTable
from .senttaskruntable import SentTaskRunTable
from .timedouttaskrequesttable import TimedOutTaskRequestTable
from .timedouttaskruntable import TimedOutTaskRunTable
from .timedoutworkertable import TimedOutWorkerTable
from .unpausedworkertable import UnpausedWorkerTable

@dataclass
class BookSchema(DuckDBSchema):
    SCHEMA_NAME = "book"

    TABLES = [
        CancelledTaskRequestTable,
        CompletedTaskRequestTable,
        CreatedTaskRequestTable,
        PausedWorkerTable,
        ReceivedHeartbeatTable,
        ReceivedTaskRunTable,
        RegisteredWorkerTable,
        SentTaskRunTable,
        TimedOutTaskRequestTable,
        TimedOutTaskRunTable,
        TimedOutWorkerTable,
        UnpausedWorkerTable,
    ]

    @classmethod
    def name(cls) -> str:
        return cls.SCHEMA_NAME

    @classmethod
    def tables(cls) -> list[DuckDBTable]:
        return cls.TABLES
