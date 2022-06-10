__version__ = "0.1.0"

def main():
    import sys
    from cutiepy.cli import cli_cutiepy
    sys.exit(cli_cutiepy())


from dataclasses import dataclass, field
from typing import Callable, List
from .brokers import Broker, build_broker
from .configloader import load_modes_from_config_file
from .task import Task
from .taskrequest import TaskRequest
from .workrequest import WorkRequest

@dataclass
class CutiePy:
    mode: str = "default"
    broker: Broker = field(init=False)

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
        args: List[any] = list,
        kwargs: dict[str, any] = dict,
        ) -> None:
        pass
