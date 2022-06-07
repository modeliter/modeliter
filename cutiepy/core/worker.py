from cutiepy.types import Result
from pydantic.dataclasses import dataclass
from .broker import Broker
from .task_request import TaskRequest


@dataclass
class WorkerConfig:
    pass


@dataclass
class Worker:
    worker_config: WorkerConfig
    broker: Broker


    async def start(self):
        return await self._start()


    async def _start(self):
        raise NotImplementedError


    async def _execute_task(self, *, task: TaskRequest) -> Result:
        raise NotImplementedError
