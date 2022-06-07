from pydantic.dataclasses import dataclass
from .task_request import TaskRequest
from .work_request import WorkRequest


@dataclass
class BrokerConfig:
    pass


@dataclass
class Broker:
    broker_config: BrokerConfig

    async def get_work(self, *, work_request: WorkRequest) -> TaskRequest:
        return await self._get_work(work_request=work_request)

    async def put_task_request(self, *, task_request: TaskRequest):
        return await self._put_task_request(task_request=task_request)

    async def _get_work(self, *, work_request: WorkRequest) -> TaskRequest:
        raise NotImplementedError

    async def _put_task_request(self, *, task_request: TaskRequest):
        raise NotImplementedError
