from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_stock():
    response = client.post("/stocks/", json={"name": "AAPL", "price": 150.5})
    assert response.status_code == 200
    assert response.json()["name"] == "AAPL"
    assert response.json()["price"] == 150.5


def test_read_stock():
    response = client.get("/stocks/1")
    assert response.status_code == 200
    assert response.json()["name"] == "AAPL"
    assert response.json()["price"] == 150.5
