
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_database_health_check():
    response = client.get("/health/database")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "opshub-api",
        "database": "connected",
    }
