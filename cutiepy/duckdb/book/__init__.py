from cutiepy.book.events import (
    CreatedTaskRequest,
)
from duckdb import DuckDBPyConnection, connect
import os
from pathlib import Path
from pydantic import BaseModel, Field
from .schema import (
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

class BookDB(BaseModel):
    con: DuckDBPyConnection

    class Config:
        arbitrary_types_allowed = True

    def create_schema(self):
        BookSchema.create(con=self.con)

    def insert_created_task_request(
        self,
        *,
        created_task_request: CreatedTaskRequest,
    ):
        query_insert = f"""
        INSERT INTO {CreatedTaskRequestTable.table_name()} (
            created_task_request_at,
            task_request_id,
            function_pickle,
            args_pickle,
            kwargs_pickle,
            max_retries_on_time_out,
            max_retries_on_error
        ) VALUES (
            :created_task_request_at,
            :task_request_id,
            :function_pickle,
            :args_pickle,
            :kwargs_pickle,
            :max_retries_on_time_out,
            :max_retries_on_error
        )
        """
        self.con.execute(query_insert, created_task_request.dict())
