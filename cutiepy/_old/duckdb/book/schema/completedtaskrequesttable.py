from cutiepy.duckdb import DuckDBTable

class CompletedTaskRequestTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "completed_task_request"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "completed_task_request_at TIMESTAMPTZ",
            "task_request_id VARCHAR",
        ]
