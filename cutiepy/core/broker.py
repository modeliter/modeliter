from pydantic.dataclasses import dataclass
from .task_run import TaskRun
from .work_request import WorkRequest


@dataclass
class BrokerConfig:
    pass


@dataclass
class Broker:
    broker_config: BrokerConfig

    async def get_work(self, *, work_request: WorkRequest) -> TaskRun:
        return await self._get_work(work_request=work_request)

    async def put_task_run(self, *, task_run: TaskRun):
        return await self._put_task_run(task_run=task_run)

    async def _get_work(self, *, work_request: WorkRequest) -> TaskRun:
        raise NotImplementedError

    async def _put_task_run(self, *, task_run: TaskRun):
        raise NotImplementedError
