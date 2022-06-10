from pydantic.dataclasses import dataclass, Field
from datetime import datetime, timezone
from pathlib import Path
import uuid

from cutiepy.taskrequest import TaskRequest
from cutiepy.taskrun import TaskRun
from cutiepy.workrequest import WorkRequest
from cutiepy.types import Error, Ok, Result
from sqlalchemy import create_engine
from .broker import Broker, BrokerConfig


@dataclass
class SQLiteBrokerConfig(BrokerConfig):
    path: Path

@dataclass
class SQLiteBroker(Broker):
    broker_config: SQLiteBrokerConfig

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
