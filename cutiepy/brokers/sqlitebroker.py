from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

from cutiepy.core import Broker, TaskRequest, TaskRun, WorkRequest
from cutiepy.types import Error, Ok, Result
from sqlalchemy import create_engine




@dataclass
class SQLiteBroker(Broker):
    sqlite_uri: str
    task_requests: list[TaskRequest] = field(default_factory=list)

    async def _get_work(self, *, work_request: WorkRequest) -> Result:
        if len(self.task_requests) == 0:
            return Error("No task requests are waiting.")

        task_request = self.task_requests.pop()
        task_run = TaskRun(
            id=uuid.uuid4().hex,
            task=task_request.task,
            broker_ref=uuid.uuid4(),
            worker_ref=work_request.worker_ref,
            broker_created_at=datetime.now(timezone.utc),
        )
        return Ok(task_run)


    async def _put_task_run(self, *, task_run: TaskRun):
        raise NotImplementedError
