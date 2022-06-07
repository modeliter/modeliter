from cutiepy.core import Broker
from pydantic.dataclasses import dataclass


@dataclass
class InProcessBroker(Broker):
    pass
