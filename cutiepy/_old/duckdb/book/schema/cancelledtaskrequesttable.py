from cutiepy.duckdb import DuckDBTable

class CancelledTaskRequestTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "cancelled_task_request"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "cancelled_task_request_at TIMESTAMPTZ",
            "task_request_id VARCHAR",
        ]
