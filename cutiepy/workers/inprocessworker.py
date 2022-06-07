from cutiepy.core.broker import Broker
from cutiepy.core.worker import Worker, WorkerConfig
from cutiepy.types import Error, Ok, Result


class InProcessWorker(Worker):
    async def _run(self):
        while True:
            task = await self.broker.pop_task()
            result = await self._execute_task(task=task)
            await self.broker.put_task_result(task, result)


    async def _execute_task(self, *, task) -> Result:
        try:
            output = task.f(*task.task_args, **task.task_kwargs)
            result = Ok(value=output)
        except Exception as e:
            result = Error(value=e)
        
        return result
