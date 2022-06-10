from cutiepy.types import Tags
from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class Task:
    f: Callable

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
