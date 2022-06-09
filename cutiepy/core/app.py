import asyncio
from pydantic.dataclasses import dataclass
from typing import Callable
from .broker import Broker
from .dashboardserver import DashboardServer
from .supervisor import Supervisor
from .task import Task


@dataclass
class App:
    broker: Broker
    supervisor: Supervisor

    async def start(self):
        await asyncio.wait([self.supervisor.start()])

    async def task(self, f: Callable) -> Task:
        broker = self.broker
        return Task(broker=broker, f=f)
