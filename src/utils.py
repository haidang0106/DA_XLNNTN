import os
from preprocessing import preprocess_dataset
from feature_engineering import build_features
from train import train_model
from evaluate import evaluate_model
from data_downloader import create_mock_vietnamese_news_dataset

def run_pipeline():
    print("="*50)
    print("BẮT ĐẦU CHẠY PIPELINE NLP PHÂN LOẠI VĂN BẢN")
    print("="*50)
    
    # Paths
    raw_path = os.path.join("data", "raw", "vietnamese_news.csv")
    processed_path = os.path.join("data", "processed", "vietnamese_news_cleaned.csv")
    models_dir = "models"
    
    # 1. Download / Create Data
    print("\n[Bước 1] Chuẩn bị dữ liệu...")
    if not os.path.exists(raw_path):
        create_mock_vietnamese_news_dataset(raw_path)
    else:
        print(f"Dataset already exists at {raw_path}")
        
    # 2. Preprocess
    print("\n[Bước 2] Tiền xử lý dữ liệu...")
    if not os.path.exists(processed_path):
         preprocess_dataset(raw_path, processed_path)
    else:
         print(f"Preprocessed data already exists at {processed_path}")
         
    # 3. Kỹ thuật rút trích & Huấn luyện
    print("\n[Bước 3 & 4] Trích xuất đặc trưng và Huấn luyện mô hình cơ bản (Naive Bayes, TF-IDF)...")
    # Tự động huấn luyện mô hình default: naive_bayes với tf-idf
    train_model('naive_bayes', 'tfidf')
    
    # 4. Đánh giá
    print("\n[Bước 5] Đánh giá mô hình trên toàn tập dữ liệu...")
    evaluate_model('naive_bayes', 'tfidf')
    
    print("\n" + "="*50)
    print("PIPELINE HOÀN TẤT THÀNH CÔNG!")
    print("Kiểm tra thư mục `models/` và `reports/` để xem kết quả.")
    print("="*50)

if __name__ == "__main__":
    run_pipeline()

