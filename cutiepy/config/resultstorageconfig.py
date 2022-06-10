from pydantic.dataclasses import dataclass


@dataclass
class ResultStorageConfig:
    type: str
    path: str
