from cutiepy.httpserver import routing
from cutiepy.core import Broker
from starlette.applications import Starlette
from uvicorn import Config, Server


class MyServer(Server):
    config: Config

    async def run(self, sockets=None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)


def build_http_server(*, broker: Broker, debug=False):
    routes = routing.build_routes(broker=broker)
    app = Starlette(
        debug=debug,
        routes=routes,
    )
    config = Config(
        app=app,
        host="127.0.0.1",
        port=8000,
        log_level="info",
    )
    return MyServer(config=config)
