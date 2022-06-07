from cutiepy.core import Task, Worker, WorkRequest
from cutiepy.types import Error, Ok, Result


class InProcessWorker(Worker):
    async def _start(self):
        broker = self.broker

        while True:
            work_request = WorkRequest(worker_ref="Me!")
            task_run = await broker.get_work(work_request=work_request)
            task = task_run.task
            result = await self._execute_task(task=task)
            task_run.result = result
            await broker.put_task_run(task_run=task_run)


    async def _execute_task(self, *, task: Task) -> Result:
        try:
            output = task.f(*task.args, **task.kwargs)
            result = Ok(value=output)
        except Exception as e:
            result = Error(value=e)
        
        return result
