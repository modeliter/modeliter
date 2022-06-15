from cutiepy.broker.http_api import build_broker_http_api_app as build_app
from cutiepy.broker.services import build_broker_service
from cutiepy.eventlogs import InMemoryEventLog
import cutiepy.serde as serde
import pytest
from starlette.testclient import TestClient
import uuid

@pytest.fixture
def worker():
    return {"worker_id": str(uuid.uuid4())}

@pytest.fixture
def broker_service(worker):
    event_log = InMemoryEventLog()
    broker_service = build_broker_service(event_log=event_log)
    broker_service.register_worker(worker_id=worker["worker_id"])
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

def test_route_get_tasks(test_client):
    response = test_client.get(
        url="/tasks",
    )

    assert response.status_code == 200
    response_body = response.json()
    assert isinstance(response_body["tasks"], list)

def test_create_and_then_get_tasks(test_client):
    test_route_commands_create_task(test_client)

    response = test_client.get(
        url="/tasks",
    )

    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body["tasks"]) == 1

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

def _test_function():
    pass
