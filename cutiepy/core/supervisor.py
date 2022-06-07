import asyncio
from pydantic.dataclasses import dataclass
from .broker import Broker
from .worker import Worker, WorkerConfig


@dataclass
class SupervisorConfig:
    worker_config: WorkerConfig
    num_workers: int = 3


@dataclass
class Supervisor:
    supervisor_config: SupervisorConfig
    broker: Broker

    async def run(self):
        worker_config = self.supervisor_config.worker_config
        workers_coroutines = [
            Worker(worker_config=worker_config).run()
            for _ in range(self.supervisor_config.num_workers)
        ]
        await asyncio.gather(*workers_coroutines)