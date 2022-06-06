from starlette.applications import Starlette

from modeliter.httpserver import routing


def create_app(*, debug=False):
    return Starlette(
        debug=debug,
        routes=routing.routes,
    )
