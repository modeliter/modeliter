from abc import ABC, abstractclassmethod
from duckdb import DuckDBPyConnection

class DuckDBTable(ABC):
    @abstractclassmethod
    def table_name(cls) -> str: pass

    @abstractclassmethod
    def columns(cls) -> list[str]: pass

    @classmethod
    def create(cls, *, con: DuckDBPyConnection):
        query_create_table = f"""
        CREATE TABLE IF NOT EXISTS {cls.table_name()} (
            {', '.join(cls.columns())}
        )
        """
        con.execute(query_create_table)
