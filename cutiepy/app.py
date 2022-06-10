from pydantic.dataclasses import dataclass
from typing import Callable
from .broker import Broker
from .task import Task


@dataclass
class App:
    broker: Broker

    def task(self, f: Callable) -> Task:
        # TODO: Save task to registry.
        return Task(f=f)
