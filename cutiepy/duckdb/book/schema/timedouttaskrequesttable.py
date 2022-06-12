from cutiepy.duckdb import DuckDBTable

class TimedOutTaskRequestTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "timed_out_task_request"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "timed_out_task_request_at TIMESTAMPTZ",
            "task_request_id VARCHAR",
        ]

