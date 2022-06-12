from datetime import datetime
import duckdb
import pickle
from cutiepy.book import events
from cutiepy.duckdb.book import BookDB

con = duckdb.connect(":memory:")
book_db = BookDB(con=con)
book_db.create_schema()

event_created_task_request = events.CreatedTaskRequest(
    created_task_request_at=datetime.now(),
    task_request_id="task_request_id-0",
    function_pickle=pickle.dumps(lambda x: print(x)),
    args_pickle=pickle.dumps(["Hello, CutiePy!"]),
    kwargs_pickle=pickle.dumps({}),
    max_retries_on_time_out=3,
    max_retries_on_error=3,
)

book_db.insert(event_created_task_request)
