from pathlib import Path
from pydantic.dataclasses import dataclass
from .resultstorage import ResultStorage, ResultStorageConfig


@dataclass
class SQLiteResultStorageConfig(ResultStorageConfig):
    path: Path


@dataclass
class SQLiteResultStorage(ResultStorage):
    config: SQLiteResultStorageConfig
