from cutiepy.core import DashboardServer
from cutiepy.httpserver import build_http_server
from multiprocessing import Process
from uvicorn import Config, Server


class InProcessDashboardServer(DashboardServer):
    async def _start(self):
        debug = self.dashboard_server_config.debug
        http_server = build_http_server(
            broker=self.broker,
            debug=debug,
        )
        http_server.run()