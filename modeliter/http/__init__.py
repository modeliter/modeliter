from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.requests import Request
from starlette.routing import Route

from modeliter.http.routes import routes


def create_app(*, debug=False):
    return Starlette(
        debug=debug,
        routes=routes,
    )
