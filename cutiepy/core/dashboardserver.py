from pydantic.dataclasses import dataclass
from .broker import Broker
from .supervisor import Supervisor


@dataclass
class DashboardServerConfig:
    type: str
    debug: bool = False


@dataclass
class DashboardServer:
    dashboard_server_config: DashboardServerConfig
    broker: Broker
    supervisor: Supervisor

    async def start(self, port):
        return await self._start(port)

    async def _start(self):
        raise NotImplementedError
