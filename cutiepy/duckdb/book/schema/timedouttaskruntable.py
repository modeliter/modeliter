from cutiepy.duckdb import DuckDBTable

class TimedOutTaskRunTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "timed_out_task_run"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "timed_out_task_run_at TIMESTAMPTZ",
            "task_run_id VARCHAR",
        ]
