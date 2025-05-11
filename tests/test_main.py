from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_item():
    response = client.post("/items", json={
        "id": 1,
        "name": "Test Item",
        "price": 9.99,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
