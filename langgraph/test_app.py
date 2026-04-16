```
import pytest
from app import app
from models import TodoItem

@pytest.fixture
def client():
    return app.test_client()

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json) == 0

def test_post_task(client):
    task_data = {'title': 'Test Task', 'description': 'This is a test task'}
    response = client.post('/tasks', json=task_data)
    assert response.status_code == 201
    assert 'id' in response.json

def test_get_task(client):
    task_data = {'title': 'Test Task', 'description': 'This is a test task'}
    response = client.post('/tasks', json=task_data)
    task_id = int(response.json['id'])
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert 'id' in response.json

def test_update_task(client):
    task_data = {'title': 'Test Task', 'description': 'This is a test task'}
    response = client.post('/tasks', json=task_data)
    task_id = int(response.json['id'])
    new_task_data = {'title': 'Updated Test Task'}
    response = client.put(f'/tasks/{task_id}', json=new_task_data)
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Test Task'

def test_delete_task(client):
    task_data = {'title': 'Test Task', 'description': 'This is a test task'}
    response = client.post('/tasks', json=task_data)
    task_id = int(response.json['id'])
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204
```