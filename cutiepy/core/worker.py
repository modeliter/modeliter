from cutiepy.types import Result
from pydantic.dataclasses import dataclass
from .broker import Broker
from .taskrequest import TaskRequest


@dataclass
class WorkerConfig:
    type: str


@dataclass
class Worker:
    worker_config: WorkerConfig
    broker: Broker


    async def start(self):
        return await self._start()


    async def _start(self):
        raise NotImplementedError
