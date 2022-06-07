from pydantic.dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, TypeAlias
from cutiepy.types import Tags


@dataclass
class Task:
    f: Callable
    args: List[Any] = []
    kwargs: Dict[str, Any] = {}
    tags: Tags = {}
    max_run_retries: int = 0
    per_run_timeout_seconds: int = 0
    per_request_timeout_seconds: int = 0
    cron_schedule: Optional[str] = None
