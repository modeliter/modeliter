from dataclasses import dataclass
from typing import Callable


@dataclass
class Task:
    f: Callable

    def f_name(self,):
        return f"{self.f.__module__}.{self.f.__qualname__}"

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
