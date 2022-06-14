from dataclasses import dataclass
from typing import Callable


@dataclass
class Task:
    f: Callable

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
