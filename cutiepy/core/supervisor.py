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

    async def start(self):
        return await self._start()

    async def _start(self):
        raise NotImplementedError
