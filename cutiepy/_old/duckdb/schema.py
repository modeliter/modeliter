from abc import ABC, abstractclassmethod
from duckdb import DuckDBPyConnection
from .table import DuckDBTable

class DuckDBSchema(ABC):
    @abstractclassmethod
    def tables(cls) -> list[DuckDBTable]: pass

    @classmethod
    def create(cls, *, con: DuckDBPyConnection):
        for table in cls.tables():
            print(f"Creating table {table.table_name()}")
            table.create(con=con)
