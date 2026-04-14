import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_all_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Buy milk"})
    assert response.status_code == 201
    assert "task_id" in response.get_json()

def test_get_task(client):
    client.post("/tasks", json={"title": "Buy milk"})
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Buy milk"

def test_update_task(client):
    client.post("/tasks", json={"title": "Buy milk"})
    response = client.put("/tasks/1", json={"title": "Buy bread"})
    assert response.status_code == 200
    assert response.get_json()["title"] == "Buy bread"

def test_delete_task(client):
    client.post("/tasks", json={"title": "Buy milk"})
    response = client.delete("/tasks/1")
    assert response.status_code == 204

def test_get_nonexistent_task(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404