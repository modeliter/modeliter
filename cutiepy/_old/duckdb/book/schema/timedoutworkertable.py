from cutiepy.duckdb import DuckDBTable

class TimedOutWorkerTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "timed_out_worker"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "timed_out_worker_at TIMESTAMPTZ",
            "worker_id VARCHAR",
        ]
