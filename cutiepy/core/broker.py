from cutiepy.types import Result
from pydantic.dataclasses import dataclass


@dataclass
class BrokerConfig:
    pass


@dataclass
class Broker:
    broker_config: BrokerConfig

    async def pop_task(self):
        raise NotImplementedError

    async def put_task_result(self, *, task, result: Result):
        raise NotImplementedError
