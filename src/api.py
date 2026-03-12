"""
FastAPI backend cho hệ thống phân loại tin tức từ URL.

Luồng xử lý:
    1. Nhận URL bài báo từ client
    2. Scraper cào nội dung
    3. Tiền xử lý (clean_text)
    4. Vectorize + Model predict
    5. Trả về nhãn + độ tự tin dưới dạng JSON

Khởi chạy:
    uvicorn src.api:app --reload
"""

import os
import sys
import pickle
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Thêm src/ vào sys.path để import các module nội bộ
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from preprocessing import clean_text
from scraper import scrape_article

# ─── App & Config ───────────────────────────────────────────────────────────
MODELS_DIR = os.path.join(ROOT_DIR, "models")

# Biến global cho model và vectorizer (load 1 lần khi khởi tạo)
_model = None
_vectorizer = None
_model_name = "naive_bayes"
_method = "tfidf"


def _load_model():
    """Load model và vectorizer."""
    global _model, _vectorizer

    vectorizer_path = os.path.join(MODELS_DIR, f"{_method}_vectorizer.pkl")
    model_path = os.path.join(MODELS_DIR, f"{_model_name}_{_method}.pkl")

    if not os.path.exists(vectorizer_path):
        print(f"[WARNING] Vectorizer not found at {vectorizer_path}")
        return

    if not os.path.exists(model_path):
        print(f"[WARNING] Model not found at {model_path}")
        return

    with open(vectorizer_path, "rb") as f:
        _vectorizer = pickle.load(f)

    with open(model_path, "rb") as f:
        _model = pickle.load(f)

    print(f"[OK] Loaded model: {_model_name} | method: {_method}")


@asynccontextmanager
async def lifespan(app):
    """Load model khi server khởi động."""
    _load_model()
    yield


app = FastAPI(
    title="NLP News Classifier API",
    description="API phân loại tin tức tiếng Việt từ URL bài báo",
    version="1.0.0",
    lifespan=lifespan,
)

class PredictRequest(BaseModel):
    """Schema cho request dự đoán."""
    url: str = Field(..., description="URL bài báo cần phân loại")


class PredictResponse(BaseModel):
    """Schema cho response dự đoán."""
    url: str
    title: str
    label: str
    confidence: float
    cleaned_text_preview: str = ""


class HealthResponse(BaseModel):
    """Schema cho health check."""
    status: str
    model_loaded: bool
    model_name: str
    method: str


# ─── Endpoints ──────────────────────────────────────────────────────────────
@app.get("/health", response_model=HealthResponse)
def health_check():
    """Kiểm tra sức khỏe server và trạng thái model."""
    return HealthResponse(
        status="ok",
        model_loaded=(_model is not None and _vectorizer is not None),
        model_name=_model_name,
        method=_method,
    )


@app.post("/predict", response_model=PredictResponse)
def predict_from_url(request: PredictRequest):
    """
    Nhận URL bài báo, cào nội dung, phân loại và trả kết quả.

    - Scrape nội dung từ URL
    - Tiền xử lý văn bản
    - Dự đoán nhãn phân loại
    """
    # Kiểm tra model đã load chưa
    if _model is None or _vectorizer is None:
        raise HTTPException(
            status_code=503,
            detail="Model chưa được tải. Hãy chạy train.py trước khi khởi động server.",
        )

    # 1. Cào nội dung
    scraped = scrape_article(request.url)
    if scraped["error"]:
        raise HTTPException(status_code=400, detail=scraped["error"])

    raw_text = scraped["content"]
    if not raw_text:
        raise HTTPException(
            status_code=400,
            detail="Không trích xuất được nội dung từ URL này.",
        )

    # 2. Tiền xử lý
    cleaned = clean_text(raw_text)
    if not cleaned:
        raise HTTPException(
            status_code=400,
            detail="Văn bản sau tiền xử lý bị rỗng, không thể phân loại.",
        )

    # 3. Vectorize
    X_features = _vectorizer.transform([cleaned])

    # 4. Dự đoán
    prediction = _model.predict(X_features)[0]

    # Tính confidence nếu model hỗ trợ
    confidence = 0.0
    if hasattr(_model, "predict_proba"):
        probabilities = _model.predict_proba(X_features)[0]
        confidence = round(float(max(probabilities)) * 100, 2)

    return PredictResponse(
        url=request.url,
        title=scraped["title"],
        label=prediction,
        confidence=confidence,
        cleaned_text_preview=cleaned[:200] + "..." if len(cleaned) > 200 else cleaned,
    )
