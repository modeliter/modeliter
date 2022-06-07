import asyncio
from pydantic.dataclasses import dataclass
from .dashboardserver import DashboardServer
from .supervisor import Supervisor


@dataclass
class App:
    supervisor: Supervisor
    dashboard_server: DashboardServer

    async def run(self):
        await asyncio.gather(
            self.supervisor.start(),
            self.dashboard_server.start(),
        )
