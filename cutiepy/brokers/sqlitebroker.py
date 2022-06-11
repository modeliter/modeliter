import pickle
from pydantic.dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import uuid

from cutiepy.taskrequests import TaskRequest
from cutiepy.taskruns import TaskRun
from cutiepy.workrequests import WorkRequest
from cutiepy.types import Error, Ok, Result
from pydantic import Field
from .broker import Broker, BrokerConfig
from cutiepy.sql import build_engine
from cutiepy.sql.models import TaskRequestModel
from sqlalchemy.orm import Session


@dataclass
class SQLiteBrokerConfig(BrokerConfig):
    path: Path


@dataclass
class SQLiteBroker(Broker):
    broker_config: SQLiteBrokerConfig
    engine = Field(init=False)

    def __post_init__(self):
        self.engine = build_engine(path=self.broker_config.path)

    def _get_work(self, *, work_request: WorkRequest) -> Result:
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

    def _put_task_request(self, *, task_request: TaskRequest):
        task_request_model = TaskRequestModel(
            id=task_request.id,
            f_name=task_request.task.f_name(),
            args_pickled=pickle.dumps(task_request.args),
            kwargs_pickled=pickle.dumps(task_request.kwargs),
        )
        with Session(self.engine) as session:
            session.add(task_request_model)
            session.commit()


    async def _put_task_run(self, *, task_run: TaskRun):
        raise NotImplementedError
