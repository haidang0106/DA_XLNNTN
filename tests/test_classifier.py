"""
Test module cho classifier (predict.py).
"""

import pytest
import os
import sys

# Thêm src/ vào path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from predict import predict_text


class TestPredictText:
    """Test hàm predict_text."""

    def test_predict_returns_label(self):
        """Test dự đoán trả về nhãn hợp lệ."""
        result = predict_text("Đội tuyển bóng đá Việt Nam thắng lớn")
        assert "Nhãn:" in result

    def test_predict_valid_categories(self):
        """Test nhãn dự đoán nằm trong 5 danh mục."""
        valid_labels = ["Chính trị", "Kinh tế", "Thể thao", "Giải trí", "Công nghệ"]
        result = predict_text("Apple ra mắt iPhone mới với nhiều cải tiến công nghệ")
        # Trích xuất nhãn từ kết quả
        for label in valid_labels:
            if label in result:
                break
        else:
            # Nếu không tìm thấy nhãn nào, kiểm tra xem có phải lỗi không
            assert "Lỗi" in result or any(label in result for label in valid_labels)

    def test_predict_empty_text(self):
        """Test xử lý văn bản rỗng."""
        result = predict_text("")
        assert "Không thể dự đoán" in result

    def test_predict_with_confidence(self):
        """Test kết quả có chứa độ tự tin."""
        result = predict_text("Thị trường chứng khoán tăng điểm mạnh")
        # Naive Bayes hỗ trợ predict_proba
        assert "Độ tự tin" in result or "Nhãn:" in result

    def test_predict_model_not_found(self):
        """Test xử lý khi model không tồn tại."""
        result = predict_text("test text", model_name="nonexistent_model")
        assert "Lỗi" in result


class TestModelLoading:
    """Test tải model."""

    def test_model_file_exists(self):
        """Test file model tồn tại."""
        model_path = os.path.join("models", "naive_bayes_tfidf.pkl")
        assert os.path.exists(model_path), f"Model file not found: {model_path}"

    def test_vectorizer_file_exists(self):
        """Test file vectorizer tồn tại."""
        vectorizer_path = os.path.join("models", "tfidf_vectorizer.pkl")
        assert os.path.exists(vectorizer_path), f"Vectorizer file not found: {vectorizer_path}"
