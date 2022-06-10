from pydantic.dataclasses import dataclass
from cutiepy.types import Error, Ok, Result
from cutiepy.task import Task
from cutiepy.workrequest import WorkRequest

@dataclass
class WorkerConfig:
    pass


@dataclass
class Worker:
    worker_config: WorkerConfig

    def _start(self):
        broker = self.broker

        while True:
            work_request = WorkRequest(worker_ref="Me!")
            result = broker.get_work(work_request=work_request)
            if isinstance(result, Error):
                print(result.value)
                continue

            task_run = result.value
            task = task_run.task
            result = self._execute_task(task=task)
            task_run.result = result
            broker.put_task_run(task_run=task_run)


    def _execute_task(self, *, task: Task) -> Result:
        try:
            output = task.f(*task.args, **task.kwargs)
            result = Ok(value=output)
        except Exception as e:
            result = Error(value=e)
        
        return result
