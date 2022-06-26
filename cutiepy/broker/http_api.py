import asyncio
from cutiepy.broker.services import BrokerService
from cutiepy.broker.errors import (
    WorkerDroppedError,
    WorkerNotRegisteredError,
)
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.responses import JSONResponse, Response
from starlette.requests import Request
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket
from typing import Callable

def build_broker_http_api_app(broker_service: BrokerService) -> Starlette:
    routes = _build_routes(broker_service=broker_service)
    return Starlette(routes=routes)

def _build_routes(broker_service: BrokerService) -> list[Route | WebSocketRoute]:
    return [
        Route(
            methods=["GET"],
            path="/tasks",
            endpoint=_query_tasks_handler(broker_service=broker_service),
        ),
        Route(
            methods=["POST"],
            path="/commands/create_task",
            endpoint=_command_create_task_handler(broker_service=broker_service),
        ),
        Route(
            methods=["POST"],
            path="/commands/register_worker",
            endpoint=_command_register_worker_handler(broker_service=broker_service),
        ),
        Route(
            methods=["POST"],
            path="/commands/send_worker_heartbeat",
            endpoint=_command_send_worker_heartbeat_handler(broker_service=broker_service),
        ),
        WebSocketRoute(
            path="/ws/task_runs",
            endpoint=_task_runs_websocket_handler(broker_service=broker_service),
        ),
    ]

def _query_tasks_handler(broker_service: BrokerService) -> Callable[[Request], Response]:
    async def handle_query_tasks(request: Request) -> Response:
        tasks = broker_service.tasks()
        return JSONResponse({"tasks": tasks})

    return handle_query_tasks

def _command_create_task_handler(broker_service: BrokerService) -> Callable[[Request], Response]:
    async def handle_command_create_task(request: Request) -> Response:
        body = await request.json()
        task_id = body["task_id"]
        function_serialized = body["function_serialized"]

        task = broker_service.create_task(
            task_id=task_id,
            function_serialized=function_serialized,
        )

        return JSONResponse({"task": task})

    return handle_command_create_task

def _command_register_worker_handler(broker_service: BrokerService) -> Callable[[Request], Response]:
    async def handle_command_register_worker(request: Request) -> Response:
        body = await request.json()
        worker_id = body["worker_id"]

        worker = broker_service.register_worker(
            worker_id=worker_id,
        )

        return JSONResponse({"worker": worker})

    return handle_command_register_worker

def _command_send_worker_heartbeat_handler(broker_service: BrokerService) -> Callable[[Request], Response]:
    async def handle_command_send_worker_heartbeat_handler(request: Request) -> Response:
        body = await request.json()
        worker_id = body["worker_id"]

        worker = broker_service.send_worker_heartbeat(
            worker_id=worker_id,
        )

        return JSONResponse({"worker": worker})

    return handle_command_send_worker_heartbeat_handler

def _task_runs_websocket_handler(broker_service: BrokerService) -> WebSocketEndpoint:
    class TaskRunsWebsocketEndpoint(WebSocketEndpoint):
        encoding: str = "json"
        worker_id: str

        async def on_connect(self, websocket: WebSocket) -> None:
            await websocket.accept()
            print("Server: Connected to client!")

        async def on_receive(self, websocket: WebSocket, data: any) -> None:
            print("Server: Received data from client!")
            message_type: str = data["message_type"]
            message: dict = data["message"]
            match message_type:
                case "init_worker_id":
                    print("Server: Received init_worker_id.")
                    worker_id = message["worker_id"]
                    self.worker_id = worker_id
                case "return_task_run":
                    print("Server: Received return_task_run.")
                    worker_id = message["worker_id"]
                    task_run_id = message["task_run_id"]
                    started_at = message["started_at"]
                    finished_at = message["finished_at"]
                    broker_service.return_task_run(
                        worker_id=worker_id,
                        task_run_id=task_run_id,
                        started_at=started_at,
                        finished_at=finished_at,
                    )

            task_run = None
            while task_run is None:
                try:
                    task_run = broker_service.assign_task_run(
                        worker_id=worker_id,
                    )
                except (WorkerDroppedError, WorkerNotRegisteredError) as e:
                    print(f"Server: {str(e)}. Closing connection.")
                    await websocket.close()
                    return
                
                if task_run is not None:
                    print("Server: Assigned a task run.")
                    await websocket.send_json(task_run)
                    return

                print("Server: No compatible task runs. Sleeping and trying again.")
                await asyncio.sleep(1)

        async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
            print("Server: Disconnected from client.")

    return TaskRunsWebsocketEndpoint
