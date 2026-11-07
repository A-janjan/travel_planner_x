"""HTTP smoke tests for the development web app."""

from fastapi.testclient import TestClient

from main import app


def test_health_page_and_assets():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}
        assert client.get("/").status_code == 200
        assert client.get("/static/js/main.js").status_code == 200
        assert client.get("/static/css/styles.css").status_code == 200
