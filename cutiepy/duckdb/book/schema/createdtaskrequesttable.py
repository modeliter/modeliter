from cutiepy.duckdb import DuckDBTable

class CreatedTaskRequestTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "created_task_request"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "created_task_request_at TIMESTAMPTZ",
            "task_request_id VARCHAR",
            "function_pickle BLOB",
            "args_pickle BLOB",
            "kwargs_pickle BLOB",
            "max_retries_on_time_out UINTEGER",
            "max_retries_on_error UINTEGER",
        ]
