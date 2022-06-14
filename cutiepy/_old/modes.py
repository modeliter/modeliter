from dataclasses import dataclass
from cutiepy.brokers import BrokerConfig
from cutiepy.resultstorages import ResultStorageConfig
from cutiepy.workers import WorkerConfig


@dataclass
class Mode:
    broker: BrokerConfig
    result_storage: ResultStorageConfig
    workers: list[WorkerConfig]
