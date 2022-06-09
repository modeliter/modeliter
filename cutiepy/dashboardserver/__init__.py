from cutiepy.dashboardserver import routing
from cutiepy.core import Broker
from starlette.applications import Starlette
from uvicorn import Config, Server


def build_app(*, broker: Broker, debug=False):
    routes = routing.build_routes(broker=broker)
    app = Starlette(
        debug=debug,
        routes=routes,
    )
    return app
