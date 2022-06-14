from dataclasses import asdict
from cutiepy.book.events import (
    CreatedTaskRequestEvent,
)
from duckdb import DuckDBPyConnection
from pydantic import BaseModel
from cutiepy.book.events import BookEvent
from cutiepy.duckdb.book.schema import (
    BookSchema,
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
)

class DuckDBBook:
    con: DuckDBPyConnection

    def __init__(self, *, con: DuckDBPyConnection):
        self.con = con
        self.create_schema()

    def create_schema(self):
        BookSchema.create(con=self.con)

    def handle_event(self, event: BookEvent):
        match event:
            case CreatedTaskRequestEvent():
                self._insert_created_task_request(event)
            case _:
                raise NotImplementedError
                


    def _insert_created_task_request(self, event: CreatedTaskRequestEvent):
        query = f"""
        INSERT INTO {CreatedTaskRequestTable.table_name()} (
            created_task_request_at,
            task_request_id,
            function_pickle,
            args_pickle,
            kwargs_pickle,
            max_retries_on_time_out,
            max_retries_on_error
        ) VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        params = [
            event.created_task_request_at,
            event.task_request_id,
            event.function_pickle,
            event.args_pickle,
            event.kwargs_pickle,
            event.max_retries_on_error,
            event.max_retries_on_time_out,
        ]
        self.con.execute(query, params)
