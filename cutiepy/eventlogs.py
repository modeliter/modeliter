from abc import ABC, abstractmethod
from pydantic.dataclasses import dataclass

@dataclass
class EventLog(ABC):
    @abstractmethod
    def append(self, event: dict):
        raise NotImplementedError("This method should be implemented by a subclass.")

    @abstractmethod
    def events(self) -> list[dict]:
        raise NotImplementedError("This method should be implemented by a subclass.")

class InMemoryEventLog(EventLog):
    _events: list[dict]

    def __init__(self):
        self._events = []

    def append(self, event: dict):
        self._events.append(event)
    
    def events(self) -> list[dict]:
        return self._events
