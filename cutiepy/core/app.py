import asyncio
from pydantic.dataclasses import dataclass
from typing import Callable
from .broker import Broker
from .dashboardserver import DashboardServer
from .task import Task


@dataclass
class App:
    broker: Broker

    async def start(self):
        await asyncio.wait([self.supervisor.start()])

    async def task(self, f: Callable) -> Task:
        broker = self.broker
        return Task(broker=broker, f=f)
