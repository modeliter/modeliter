from pydantic.dataclasses import dataclass
from .broker import Broker
from .supervisor import Supervisor


@dataclass
class DashboardServerConfig:
    pass


@dataclass
class DashboardServer:
    dashboard_server_config: DashboardServerConfig
    broker: Broker
    supervisor: Supervisor

    async def start(self):
        return await self._start()

    async def _start(self):
        raise NotImplementedError
