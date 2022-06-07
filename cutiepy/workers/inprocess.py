from cutiepy.core.broker import Broker
from cutiepy.core.worker import Worker, WorkerConfig
from cutiepy.types import Error, Ok
from pydantic.dataclasses import dataclass


@dataclass
class InProcessWorker(Worker):
    worker_config: WorkerConfig
    broker: Broker

    async def run(self):
        while True:
            task = await self.broker.pop_task()
            try:
                output = task.f(*task.task_args, **task.task_kwargs)
                result = Ok(value=output)
            except Exception as e:
                result = Error(value=e)
            finally:
                await self.broker.put_task_result(task, result)
