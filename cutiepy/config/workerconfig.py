from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class WorkerConfig:
    capabilities: dict = Field(default_factory=dict)
    preferences: dict = Field(default_factory=dict)
