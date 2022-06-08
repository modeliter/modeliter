from cutiepy.core import Broker
from cutiepy.httpserver import frontend, api
from starlette.routing import Route, Mount


def build_routes(*, broker: Broker):
    return [
        Route(
            path="/api/v1/names",
            endpoint=api.get_names,
            methods=["GET"],
        ),
        Route(
            path="/api/v1/names",
            endpoint=api.post_name(),
            methods=["POST"],
        ),
        Mount(
            path="/",
            app=frontend.static_files,
        )
    ]
