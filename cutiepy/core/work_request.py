from pydantic.dataclasses import dataclass
from cutiepy.types import Tags


@dataclass
class WorkRequest:
    worker_ref: str
    capability_tags: Tags = {}
    preference_tags: Tags = {}
