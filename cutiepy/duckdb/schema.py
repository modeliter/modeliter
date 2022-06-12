from abc import ABC, abstractclassmethod
from duckdb import DuckDBPyConnection
from .table import DuckDBTable

class DuckDBSchema(ABC):
    @abstractclassmethod
    def name(cls) -> str: pass

    @abstractclassmethod
    def tables(cls) -> list[DuckDBTable]: pass

    @classmethod
    def create(cls, *, con: DuckDBPyConnection):
        query_create_schema = f"""
        CREATE SCHEMA IF NOT EXISTS {cls.name()};
        """
        con.execute(query_create_schema)

        for table in cls.tables():
            table.create(con=con, schema=cls.name())
