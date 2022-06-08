from pydantic.dataclasses import dataclass
from .broker import Broker
from .task import Task
from .taskrequest import TaskRequest


@dataclass
class BrokerClientConfig:
    pass


@dataclass
class BrokerClient:
    broker_client_config: BrokerClientConfig
    broker: Broker

    async def enqueue_task(self, *, task: Task):
        return await self._enqueue_task(task=task)

    async def _enqueue_task(self, *, task: Task):
        broker = self.broker
        task_request = TaskRequest(task=task)
        return await broker.put_task_request(task_request=task_request)
