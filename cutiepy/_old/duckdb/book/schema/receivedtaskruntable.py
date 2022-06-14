from cutiepy.duckdb import DuckDBTable

class ReceivedTaskRunTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "received_task_run"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "received_task_run TIMESTAMPTZ",
            "task_run_id VARCHAR",
            "worker_id VARCHAR",
            "started_by_worker_at TIMESTAMPTZ",
            "finished_by_worker_at TIMESTAMPTZ",
            "task_result_pickle BLOB",
        ]
