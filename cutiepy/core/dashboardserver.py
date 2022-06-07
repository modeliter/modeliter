import asyncio
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

    async def run(self):
        raise NotImplementedError
