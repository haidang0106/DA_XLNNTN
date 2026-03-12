"""
Test module cho API (api.py).
Sử dụng TestClient của FastAPI (dựa trên httpx).
"""

import pytest
import sys
import os
from unittest.mock import patch

# Thêm src/ vào path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fastapi.testclient import TestClient
from api import app


@pytest.fixture
def client():
    """Tạo test client cho FastAPI app."""
    with TestClient(app) as c:
        yield c


class TestHealthEndpoint:
    """Test endpoint /health."""

    def test_health_returns_ok(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_health_model_info(self, client):
        response = client.get("/health")
        data = response.json()
        assert "model_loaded" in data
        assert "model_name" in data
        assert "method" in data


class TestPredictEndpoint:
    """Test endpoint /predict."""

    def test_predict_missing_url(self, client):
        """Test gửi request thiếu URL."""
        response = client.post("/predict", json={})
        assert response.status_code == 422  # Validation error

    def test_predict_invalid_url(self, client):
        """Test gửi URL không hợp lệ."""
        response = client.post("/predict", json={"url": "not-a-url"})
        assert response.status_code == 400

    @patch("api.scrape_article")
    def test_predict_successful(self, mock_scrape, client):
        """Test dự đoán thành công (mock scraper)."""
        mock_scrape.return_value = {
            "title": "Tin thể thao",
            "content": "Đội tuyển bóng đá Việt Nam giành chiến thắng trong trận đấu quan trọng tại vòng loại World Cup",
            "url": "https://example.com/article",
            "error": None,
        }

        response = client.post(
            "/predict", json={"url": "https://example.com/article"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "label" in data
        assert "confidence" in data
        assert "title" in data
        assert data["url"] == "https://example.com/article"

    @patch("api.scrape_article")
    def test_predict_scraper_error(self, mock_scrape, client):
        """Test xử lý lỗi từ scraper."""
        mock_scrape.return_value = {
            "title": "",
            "content": "",
            "url": "https://dead.com",
            "error": "Lỗi kết nối: Không thể truy cập URL",
        }

        response = client.post(
            "/predict", json={"url": "https://dead.com"}
        )
        assert response.status_code == 400
        assert "error" in response.json()["detail"] or "kết nối" in response.json()["detail"]
