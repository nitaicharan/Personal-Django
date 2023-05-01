from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_list():
    response = client.get("/api/articles")
    assert response.status_code == 200
