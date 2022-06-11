from cutiepy.taskrequests import TaskRequest
from cutiepy.taskruns import TaskRun
from cutiepy.workrequests import WorkRequest
from pydantic.dataclasses import dataclass


@dataclass
class Broker:
    def get_work(self, *, work_request: WorkRequest) -> TaskRun:
        return self._get_work(work_request=work_request)

    def put_task_request(self, *, task_request: TaskRequest):
        return self._put_task_request(task_request=task_request)

    def put_task_run(self, *, task_run: TaskRun):
        return self._put_task_run(task_run=task_run)

    def _get_work(self, *, work_request: WorkRequest) -> TaskRun:
        raise NotImplementedError

    def _put_task_request(self, *, task_request: TaskRequest):
        raise NotImplementedError

    def _put_task_run(self, *, task_run: TaskRun):
        raise NotImplementedError


@dataclass
class BrokerConfig:
    pass
