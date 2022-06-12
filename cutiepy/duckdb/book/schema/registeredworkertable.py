from cutiepy.duckdb import DuckDBTable

class RegisteredWorkerTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "registered_worker"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "registered_worker_at TIMESTAMPTZ",
            "worker_id VARCHAR",
        ]
