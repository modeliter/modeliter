from starlette.responses import JSONResponse, Response
from starlette.requests import Request


async def post_reverse(request: Request) -> Response:
    body_dict = await request.json()
    return JSONResponse(
        headers={
            "Content-Type": "application/json",
        },
        content={"output": body_dict["input"][::-1]},
        )
