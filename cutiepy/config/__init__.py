from pydantic.dataclasses import dataclass
from typing import List
from .brokerconfig import BrokerConfig
from .resultstorageconfig import ResultStorageConfig
from .workerconfig import WorkerConfig


@dataclass
class Mode:
    broker: BrokerConfig
    result_storage: ResultStorageConfig
    workers: List[WorkerConfig]

