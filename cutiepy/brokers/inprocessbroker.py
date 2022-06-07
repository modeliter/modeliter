from cutiepy.core import Broker, TaskRequest, WorkRequest


class InProcessBroker(Broker):
    async def _get_work(self, *, work_request: WorkRequest) -> TaskRequest:
        raise NotImplementedError

    async def _put_task_request(self, *, task_request: TaskRequest):
        raise NotImplementedError
