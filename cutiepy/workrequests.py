from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cutiepy.types import Tags
from pydantic.dataclasses import dataclass, Field


@dataclass
class WorkRequest:
    worker_ref: str
    capability_tags: Tags = Field(default_factory=dict)
    preference_tags: Tags = Field(default_factory=dict)
