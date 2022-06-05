from os import path
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

def _relative_path(rel: str) -> str:
    return path.join(path.dirname(__file__), rel)

async def index(_: Request) -> Response:
    return JSONResponse({'message': 'Hello, world!'})

routes = [
    Route("/api/v1", index),
    Mount("/", StaticFiles(directory=_relative_path("../../site"), html=True)),
]
