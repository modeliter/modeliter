from cutiepy.core import Task, TaskRequest, Worker, WorkRequest
from cutiepy.types import Error, Ok, Result


class InProcessWorker(Worker):
    async def _start(self):
        broker = self.broker

        while True:
            task_request = await broker.get_work()
            result = await self._execute_task(task=task_request.task)
            task_request.result = result
            await broker.put_task_request(task_request=task_request)


    async def _execute_task(self, *, task: Task) -> Result:
        try:
            output = task.f(*task.args, **task.kwargs)
            result = Ok(value=output)
        except Exception as e:
            result = Error(value=e)
        
        return result