from cutiepy.broker.http_api import build_broker_http_api_app as build_app
from cutiepy.broker.services import build_broker_service
from cutiepy.eventlogs import InMemoryEventLog
import cutiepy.serde as serde
import pytest
from starlette.testclient import TestClient
import uuid

@pytest.fixture
def task():
    return {
        "task_id": str(uuid.uuid4()),
        "function_serialized": serde.serialize(_test_function),
    }

@pytest.fixture
def worker():
    return {
        "worker_id": str(uuid.uuid4()),
    }

@pytest.fixture
def broker_service(task, worker):
    event_log = InMemoryEventLog()
    broker_service = build_broker_service(event_log=event_log)
    broker_service.create_task(**task)
    broker_service.register_worker(**worker)
    return broker_service

@pytest.fixture
def test_client(broker_service):
    test_client = TestClient(build_app(broker_service=broker_service))
    return test_client

def test_route_commands_create_task(test_client):
    task = {
        "task_id": str(uuid.uuid4()),
        "function_serialized": serde.serialize(_test_function),
    }
    response = test_client.post(
        url="/commands/create_task",
        json=task,
    )

    assert response.status_code == 200
    response_body = response.json()
    assert response_body["task"]["task_id"] == task["task_id"]

def test_route_get_tasks(test_client, task):
    response = test_client.get(
        url="/tasks",
    )

    assert response.status_code == 200
    response_body = response.json()
    task_ids = map(lambda task: task["task_id"], response_body["tasks"])
    assert task["task_id"] in task_ids

def test_register_worker(test_client):
    worker = {
        "worker_id": str(uuid.uuid4()),
    }
    response = test_client.post(
        url="/commands/register_worker",
        json=worker,
    )

    assert response.status_code == 200
    response_body = response.json()
    assert response_body["worker"]["worker_id"] == worker["worker_id"]

def test_send_worker_heartbeat(test_client, worker):
    response = test_client.post(
        url="/commands/send_worker_heartbeat",
        json=worker,
    )

    assert response.status_code == 200

# async def test_return_task_run(test_client, task, worker):
#     task_run = {
#         "task_run_id": str(uuid.uuid4()),
#         "worker_id": worker["worker_id"],
#         "started_at": datetime.isoformat(datetime.now(timezone.utc)),
#         "finished_at": datetime.isoformat(datetime.now(timezone.utc)),
#         "result_serialized": serde.serialize(None),
#     }
#     with handle_task_runs_websocket.websocket_connect("/ws/task_runs") as ws_task_runs:
#         ws_task_runs.send_json({"task_run": task_run})

def test_app(test_client):
    from starlette.endpoints import WebSocketEndpoint
    from starlette.routing import WebSocketRoute
    from starlette.applications import Starlette

    class Echo(WebSocketEndpoint):
        encoding = "text"

        async def on_receive(self, websocket, data):
            await websocket.send_text(f"Message text was: {data}")

    routes = [
        WebSocketRoute("/ws", Echo)
    ]

    app = Starlette(routes=routes)

    with test_client.websocket_connect('/ws/task_runs') as websocket:
        websocket.send_json({"message": "hi!"})
        data = websocket.receive_json()
        assert data == {"message": "Hello!"}

def _test_function():
    pass
