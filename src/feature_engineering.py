import pandas as pd
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def build_features(input_path, output_dir, method='tfidf'):
    """
    Trích xuất đặc trưng từ văn bản đã được làm sạch.
    Lưu Vectorizer và trả về ma trận đặc trưng (X), nhãn (y).
    """
    print(f"Loading preprocessed data from {input_path}...")
    df = pd.read_csv(input_path)
    
    # Loại bỏ các dòng có text rỗng sau khi tiền xử lý
    df = df.dropna(subset=['clean_text'])
    
    X_text = df['clean_text'].values
    y = df['label'].values
    
    print(f"Extracting features using {method.upper()}...")
    if method == 'tfidf':
        vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    elif method == 'bow':
        vectorizer = CountVectorizer(max_features=5000, ngram_range=(1, 2))
    else:
        raise ValueError("Method must be 'tfidf' or 'bow'")
        
    X_features = vectorizer.fit_transform(X_text)
    
    # Lưu vectorizer lại để dùng chung lúc dự đoán (Inference)
    os.makedirs(output_dir, exist_ok=True)
    vectorizer_path = os.path.join(output_dir, f"{method}_vectorizer.pkl")
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)
        
    print(f"Features extracted. Shape of X: {X_features.shape}")
    print(f"Vectorizer saved to {vectorizer_path}")
    
    return X_features, y, vectorizer

if __name__ == "__main__":
    processed_path = os.path.join("data", "processed", "vietnamese_news_cleaned.csv")
    models_dir = "models"
    
    if os.path.exists(processed_path):
        X, y, vec = build_features(processed_path, models_dir, method='tfidf')
    else:
        print(f"Error: {processed_path} not found. Please run preprocessing.py first.")
