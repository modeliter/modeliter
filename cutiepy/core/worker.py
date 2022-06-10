from cutiepy.types import Result
from pydantic.dataclasses import dataclass
from .broker import Broker
from .taskrequest import TaskRequest


@dataclass
class WorkerConfig:
    pass


@dataclass
class Worker:
    broker: Broker
    worker_config: WorkerConfig


    async def start(self):
        return await self._start()


    async def _start(self):
        raise NotImplementedError
