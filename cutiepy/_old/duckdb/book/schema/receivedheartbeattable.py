from cutiepy.duckdb import DuckDBTable

class ReceivedHeartbeatTable(DuckDBTable):
    @classmethod
    def table_name(cls):
        return "received_heartbeat"

    @classmethod
    def columns(cls) -> list[str]:
        return [
            "received_heartbeat_at TIMESTAMPTZ",
            "worker_id VARCHAR",
        ]
