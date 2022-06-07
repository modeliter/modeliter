from cutiepy.core import Broker, TaskRun, WorkRequest


class InProcessBroker(Broker):
    async def _get_work(self, *, work_request: WorkRequest) -> TaskRun:
        raise NotImplementedError

    async def _put_task_run(self, *, task_run: TaskRun):
        raise NotImplementedError
