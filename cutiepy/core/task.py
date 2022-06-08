from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cutiepy.types import Tags
    from typing import Callable, Optional
    from .broker import Broker
    from .taskrequest import TaskRequest
from pydantic import Field
from pydantic.dataclasses import dataclass
import uuid


@dataclass
class Task:
    broker: Broker
    f: Callable
    tags: Tags = Field(default_factory=dict)
    max_run_retries: int = 0
    per_run_timeout_seconds: int = 0
    per_request_timeout_seconds: int = 0
    cron_schedule: Optional[str] = None


    def enqueue(self, *args, **kwargs):
        task_request = TaskRequest(
            id=str(uuid.uuid4()),
            task=self,
            task_args=args,
            task_kwargs=kwargs,
        )
        broker = self.broker
        broker.put_task_request_sync(task_request=task_request)
