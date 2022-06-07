from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from pydantic.dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, TypeAlias


@dataclass
class App:
    pass


@dataclass
class Task:
    app: App
    f: Callable
    ref: str


@dataclass
class TaskRequest:
    task_ref: str
    task_args: List[Any] = []
    task_kwargs: Dict[str, Any] = {}
    tags: Dict[str, str] = {}


@dataclass
class TaskRequestWithRetries(TaskRequest):
    max_retries: int = 3


@dataclass
class TaskRequestWithTimeout(TaskRequest):
    timeout_seconds: int = 60


@dataclass
class Ok:
    value: Any


@dataclass
class Err:
    value: Exception


Result: TypeAlias = Ok | Err

@dataclass
class TaskRunStatus:
    timestamp: datetime


@dataclass
class TaskRunStatusWaiting(TaskRunStatus):
    pass

@dataclass
class TaskRunStatusRunning(TaskRunStatus):
    worker_ref: str


@dataclass
class TaskRun:
    task_request: TaskRequest
    history: List[TaskRunStatus]


@dataclass
class TaskRunWaiting(TaskRun):
    pass


