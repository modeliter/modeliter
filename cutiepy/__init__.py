__version__ = "0.1.0"

def main():
    import sys
    from cutiepy.cli import cli_cutiepy
    sys.exit(cli_cutiepy())


import pickle
import duckdb
from pydantic.dataclasses import dataclass
from typing import Callable, Optional
import uuid
from cutiepy.book import Book
from cutiepy.duckdb.book import DuckDBBook
from cutiepy.book.events import CreatedTaskRequestEvent
from datetime import datetime, timezone

class CutiePy:
    book: Book

    def __init__(self):
        con = duckdb.connect()
        self.book = DuckDBBook(con=con)

    def enqueue(
        self,
        function: Callable,
        *,
        args: Optional[list[any]] = None,
        kwargs: Optional[dict[str, any]] = None,
        ) -> None:
        created_task_request_event = CreatedTaskRequestEvent(
            created_task_request_at=datetime.now(timezone.utc),
            task_request_id=str(uuid.uuid4()),
            function_pickle=pickle.dumps(function),
            args_pickle=pickle.dumps(args),
            kwargs_pickle=pickle.dumps(kwargs),
            max_retries_on_error=0,
            max_retries_on_time_out=0,
        )
        self.book.handle_event(event=created_task_request_event)
