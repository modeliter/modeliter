from cutiepy.core import DashboardServer
from pydantic.dataclasses import dataclass

@dataclass
class InProcessDashboardServer(DashboardServer):
    pass
