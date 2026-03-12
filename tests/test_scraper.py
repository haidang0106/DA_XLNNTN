"""
Test module cho scraper.py
"""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Thêm src/ vào path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from scraper import scrape_article, _get_site_key, _extract_generic


class TestGetSiteKey:
    """Test hàm xác định trang báo."""

    def test_vnexpress(self):
        assert _get_site_key("https://vnexpress.net/bai-viet-123.html") == "vnexpress.net"

    def test_dantri(self):
        assert _get_site_key("https://dantri.com.vn/xa-hoi/bai-viet.htm") == "dantri.com.vn"

    def test_tuoitre(self):
        assert _get_site_key("https://tuoitre.vn/tin-tuc/bai-viet.htm") == "tuoitre.vn"

    def test_unknown_site(self):
        assert _get_site_key("https://example.com/page") is None


class TestScrapeArticleValidation:
    """Test validation đầu vào của scrape_article."""

    def test_empty_url(self):
        result = scrape_article("")
        assert result["error"] is not None
        assert "không hợp lệ" in result["error"]

    def test_invalid_url_no_protocol(self):
        result = scrape_article("vnexpress.net/bai-viet")
        assert result["error"] is not None
        assert "không hợp lệ" in result["error"]

    def test_none_url(self):
        result = scrape_article(None)
        assert result["error"] is not None


class TestScrapeArticleMocked:
    """Test scrape_article với mock requests."""

    @patch("scraper.requests.get")
    def test_successful_scrape_generic(self, mock_get):
        """Test cào thành công từ trang generic."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
        <head><title>Test Title</title></head>
        <body>
            <h1>Test Article Title</h1>
            <article>
                <p>Day la noi dung bai bao rat dai de co the test duoc ham scraper cua chung ta.</p>
                <p>Them mot doan nua de du do dai cho phan test noi dung bai bao hom nay.</p>
            </article>
        </body>
        </html>
        """
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = scrape_article("https://example.com/article")
        assert result["error"] is None
        assert result["title"] == "Test Article Title"
        assert len(result["content"]) > 0

    @patch("scraper.requests.get")
    def test_http_404(self, mock_get):
        """Test xử lý lỗi 404."""
        from requests.exceptions import HTTPError

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = HTTPError(response=mock_response)
        mock_get.return_value = mock_response

        result = scrape_article("https://example.com/not-found")
        assert result["error"] is not None
        assert "404" in result["error"]

    @patch("scraper.requests.get")
    def test_timeout(self, mock_get):
        """Test xử lý timeout."""
        from requests.exceptions import Timeout

        mock_get.side_effect = Timeout()

        result = scrape_article("https://example.com/slow")
        assert result["error"] is not None
        assert "Timeout" in result["error"]

    @patch("scraper.requests.get")
    def test_connection_error(self, mock_get):
        """Test xử lý lỗi kết nối."""
        from requests.exceptions import ConnectionError

        mock_get.side_effect = ConnectionError()

        result = scrape_article("https://dead-link.com/page")
        assert result["error"] is not None
        assert "kết nối" in result["error"]
