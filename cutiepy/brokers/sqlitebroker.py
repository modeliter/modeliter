import pickle
from pydantic.dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import uuid

from cutiepy.taskrequests import TaskRequest, TaskRequestStatus
from cutiepy.taskruns import TaskRun
from cutiepy.workrequests import WorkRequest
from pydantic import Field
from .broker import Broker, BrokerConfig
from cutiepy.sql import build_engine
from cutiepy.sql.models import TaskRequestModel, TaskRunModel
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

    def _get_work(self, *, work_request: WorkRequest) -> TaskRun:
        with Session(self.engine) as session:
            task_request_model = session.query(TaskRequestModel).filter(TaskRequestModel.status==TaskRequestStatus.WAITING).one_or_none()
            if task_request_model is None:
                return None

            task_run = TaskRun(
                id=str(uuid.uuid4()),
                task_request=TaskRequest.from_model(task_request_model),
                worker_ref=work_request.worker_ref,
                broker_created_at=datetime.now(timezone.utc),
            )
            task_run_model = TaskRunModel(
                id=task_run.id,
                task_request=task_request_model,
                worker_ref=task_run.worker_ref,
                broker_created_at=task_run.broker_created_at,
            )
            task_request_model.status = TaskRequestStatus.RUNNING
            session.add(task_request_model)
            session.add(task_run_model)
            session.commit()
            return task_run

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
