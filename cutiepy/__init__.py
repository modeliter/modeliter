__version__ = "0.1.0"

def main():
    import sys
    from cutiepy.cli import cli_cutiepy
    sys.exit(cli_cutiepy())


from dataclasses import dataclass
from typing import Callable, List
from .core import Task

@dataclass
class CutiePy:
    mode: str = "default"

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
