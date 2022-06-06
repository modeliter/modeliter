from starlette.responses import JSONResponse, Response
from starlette.requests import Request


async def get_index(_: Request) -> Response:
    return JSONResponse({'message': 'Hello, world!'})
