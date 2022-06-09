from typing import Callable
from starlette.responses import JSONResponse, Response
from starlette.requests import Request


async def get_names(request: Request) -> Response:
    return JSONResponse({"names": ["John", "Jane"]})

def post_name() -> Callable[[Request], Response]:
    async def _post_name(request: Request) -> Response:
        request_body_dict = await request.json()
        unsafe_name = request_body_dict["name"]

        return JSONResponse({"status": "success"})

    return _post_name
