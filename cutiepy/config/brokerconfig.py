from pydantic.dataclasses import dataclass


@dataclass
class BrokerConfig:
    type: str
    path: str
