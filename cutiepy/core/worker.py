from cutiepy.types import Error, Ok
from pydantic.dataclasses import dataclass
from .broker import Broker


@dataclass
class WorkerConfig:
    pass


@dataclass
class Worker:
    worker_config: WorkerConfig
    broker: Broker


    async def run(self):
        return await self._run()


    async def _run(self):
        raise NotImplementedError


    async def _execute_task(self, *, task):
        raise NotImplementedError
