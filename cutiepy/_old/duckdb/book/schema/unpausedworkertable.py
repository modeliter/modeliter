from cutiepy.duckdb import DuckDBTable

class UnpausedWorkerTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "unpaused_worker"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "unpaused_worker_at TIMESTAMPTZ",
            "worker_id VARCHAR",
        ]
