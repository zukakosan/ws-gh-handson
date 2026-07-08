from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_list_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 3


def test_create_todo():
    response = client.post("/todos", json={"title": "New task"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "New task"
    assert data["completed"] is False


# ハンズオンで実装するテスト（現時点では実行しない）
#
# def test_get_todo_by_id():
#     response = client.get("/todos/1")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == 1
#     assert data["title"] == "Buy groceries"
#
#
# def test_get_todo_not_found():
#     response = client.get("/todos/9999")
#     assert response.status_code == 404
