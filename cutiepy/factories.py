from core import (
    Broker, BrokerConfig,
    Worker, WorkerConfig,
)
from workers import InProcessWorker


def build_worker(*, worker_config: WorkerConfig, broker: Broker) -> Worker:
    worker_type_to_class = {
        "inprocess": InProcessWorker,
    }
    worker_constructor = worker_type_to_class[worker_config.type]
    return worker_constructor(worker_config=worker_config, broker=broker)