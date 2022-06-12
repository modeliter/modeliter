from cutiepy.duckdb import DuckDBTable

class SentTaskRunTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "sent_task_run"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "sent_task_run_at TIMESTAMPTZ",
            "task_run_id VARCHAR",
            "worker_id VARCHAR",
        ]
