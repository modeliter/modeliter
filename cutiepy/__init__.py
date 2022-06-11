__version__ = "0.1.0"

def main():
    import sys
    from cutiepy.cli import cli_cutiepy
    sys.exit(cli_cutiepy())


from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Callable, Optional
import uuid
from .brokers import Broker, build_broker
from .configloader import load_modes_from_config_file
from .tasks import Task
from .taskrequests import TaskRequest

@dataclass
class CutiePy:
    mode: str = "default"
    broker: Broker = Field(init=False)

    def __post_init__(self):
        modes = load_modes_from_config_file()
        mode = modes[self.mode]
        broker_config = mode.broker
        self.broker = build_broker(broker_config=broker_config)

    def task(self, f: Callable) -> Task:
        return Task(f=f)

    def enqueue(
        self,
        task: Task,
        *,
        args: Optional[list[any]] = None,
        kwargs: Optional[dict[str, any]] = None,
        ) -> None:
        task_request = TaskRequest(
            id=str(uuid.uuid4()),
            task=task,
            args=args if args is not None else [],
            kwargs=kwargs if kwargs is not None else {},
        )
        self.broker.put_task_request(task_request=task_request)
