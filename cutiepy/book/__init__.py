from abc import ABC, abstractmethod
from datetime import datetime
from typing import Callable, Optional
from .events import BookEvent
from .states import (
    TaskRequest,
    TaskResult,
    TaskRun,
    Worker,
)

class Book(ABC):
    @abstractmethod
    def handle_event(self, event: BookEvent): pass

    @abstractmethod
    def task_request(self, *, id: str) -> TaskRequest: pass

    @abstractmethod
    def task_result(self, *, id: str) -> TaskResult: pass

    @abstractmethod
    def task_run(self, *, id: str) -> TaskRun: pass

    @abstractmethod
    def worker(self, *, id: str) -> Worker: pass
