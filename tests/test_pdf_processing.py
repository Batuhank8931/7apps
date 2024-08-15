from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def mock_pdf_file():
    return open("tests/data/sample.pdf", "rb")

def test_pdf_upload(mock_pdf_file):
    response = client.post("/v1/pdf", files={"file": mock_pdf_file})
    assert response.status_code == 200
    assert "pdf_id" in response.json()
