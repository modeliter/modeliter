from os import path
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from modeliter.httpserver import frontend, api


routes = [
    Route(
        path="/api/v1/reverse",
        endpoint=api.post_reverse,
        methods=["POST"],
    ),
    Mount(
        path="/",
        app=frontend.static_files,
    )
]
