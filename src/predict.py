import os
import pickle
import argparse
from preprocessing import clean_text

def predict_text(text, model_name='naive_bayes', method='tfidf'):
    """
    Dự đoán thể loại của một đoạn văn bản mới.
    """
    models_dir = "models"
    
    # 1. Tiền xử lý văn bản (giống hệt lúc huấn luyện)
    cleaned = clean_text(text)
    if not cleaned:
        return "Không thể dự đoán (văn bản rỗng hoặc không hợp lệ)"
        
    # 2. Load Vectorizer
    vectorizer_path = os.path.join(models_dir, f"{method}_vectorizer.pkl")
    if not os.path.exists(vectorizer_path):
        return f"Lỗi: Không tìm thấy vectorizer tại {vectorizer_path}. Hãy chạy huấn luyện trước."
        
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
        
    # Chuyển văn bản thành vector
    X_features = vectorizer.transform([cleaned])
    
    # 3. Load Model
    model_path = os.path.join(models_dir, f"{model_name}_{method}.pkl")
    if not os.path.exists(model_path):
        return f"Lỗi: Không tìm thấy model tại {model_path}. Hãy chạy huấn luyện trước."
        
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    # 4. Dự đoán
    prediction = model.predict(X_features)[0]
    
    # Nếu model có hỗ trợ predict_proba (tính xác suất)
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_features)[0]
        max_prob = max(probabilities) * 100
        return f"Nhãn: {prediction} (Độ tự tin: {max_prob:.2f}%)"
    else:
        return f"Nhãn: {prediction}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict text category")
    parser.add_argument('--text', type=str, required=True, help='Đoạn văn bản cần phân loại')
    parser.add_argument('--model', type=str, default='naive_bayes', help='Tên model (vd: naive_bayes)')
    parser.add_argument('--method', type=str, default='tfidf', help='Tên vectorizer (vd: tfidf)')
    
    args = parser.parse_args()
    
    print(f"\nVăn bản gốc: '{args.text}'")
    result = predict_text(args.text, args.model, args.method)
    print(f"Kết quả dự đoán: {result}\n")
