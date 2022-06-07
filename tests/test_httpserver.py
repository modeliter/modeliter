from starlette.testclient import TestClient

from modeliter.httpserver import create_app


def test_it_works():
    client = TestClient(create_app())

    response = client.post("/api/v1/names", json={"name": "John"})
    assert response.status_code == 200

    response = client.get("/api/v1/names")
    assert response.status_code == 200
    assert response.json() == {"names": ["John"]}
