from cutiepy.duckdb import DuckDBTable

class PausedWorkerTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "paused_worker"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "paused_worker_at TIMESTAMPTZ",
            "worker_id VARCHAR",
        ]
