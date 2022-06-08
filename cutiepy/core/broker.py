from pydantic.dataclasses import dataclass
from .taskrequest import TaskRequest
from .taskrun import TaskRun
from .workrequest import WorkRequest


@dataclass
class BrokerConfig:
    type: str


@dataclass
class Broker:
    broker_config: BrokerConfig

    async def get_work(self, *, work_request: WorkRequest) -> TaskRun:
        return await self._get_work(work_request=work_request)

    async def put_task_request(self, *, task_request: TaskRequest):
        return await self._put_task_request(task_request=task_request)

    def put_task_request_sync(self, *, task_request: TaskRequest):
        return self._put_task_request_sync(task_request=task_request)

    async def put_task_run(self, *, task_run: TaskRun):
        return await self._put_task_run(task_run=task_run)

    async def _get_work(self, *, work_request: WorkRequest) -> TaskRun:
        raise NotImplementedError

    async def _put_task_request(self, *, task_request: TaskRequest):
        raise NotImplementedError

    def _put_task_request_sync(self, *, task_request: TaskRequest):
        raise NotImplementedError

    async def _put_task_run(self, *, task_run: TaskRun):
        raise NotImplementedError
