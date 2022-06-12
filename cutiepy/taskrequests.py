import pickle
from cutiepy.types import Result
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import Any, Optional
from cutiepy.tasks import Task
from cutiepy.sql.models import TaskRequestModel


class TaskRequestStatus(Enum):
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"


@dataclass
class TaskRequest:
    id: str
    task: Task
    args: list
    kwargs: dict[str, Any]
    status: Optional[TaskRequestStatus] = None
    result: Optional[Result] = None
    num_run_retries: int = 0

    def from_model(self, task_request_model: TaskRequestModel):
        return TaskRequest(
            id=task_request_model.id,
            task=Task(f=lambda: print("Fake f")),
            args=pickle.loads(task_request_model.args_pickled),
            kwargs=pickle.loads(task_request_model.kwargs_pickled),
            status=task_request_model.status,
            result=task_request_model.result_pickled,
        )
