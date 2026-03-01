import os
import argparse
import pickle
from sklearn.model_selection import train_test_split
from feature_engineering import build_features
from model import get_model
from sklearn.metrics import classification_report, accuracy_score
import time

def train_model(model_name, method='tfidf'):
    processed_path = os.path.join("data", "processed", "vietnamese_news_cleaned.csv")
    models_dir = "models"
    
    # 1. Load data and extract features
    X_features, y, vectorizer = build_features(processed_path, models_dir, method=method)
    
    # 2. Split dataset: 80% train, 20% test
    # Lưu ý: Trong thực tế nên chia thêm tập validation
    X_train, X_test, y_train, y_test = train_test_split(
        X_features, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 3. Get Model
    print(f"Initializing model: {model_name}...")
    model = get_model(model_name)
    
    # 4. Train Model
    start_time = time.time()
    print("Training started...")
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    print(f"Training completed in {training_time:.2f} seconds.")
    
    # 5. Evaluate on test set (Quick check)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n--- Quick Evaluation on Test Set ---")
    print(f"Accuracy: {acc:.4f}")
    
    # 6. Save Model
    model_path = os.path.join(models_dir, f"{model_name}_{method}.pkl")
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train NLP Classification Model")
    parser.add_argument('--model', type=str, default='naive_bayes', 
                        choices=['naive_bayes', 'logistic_regression', 'svm', 'random_forest'],
                        help='Name of the model to train')
    parser.add_argument('--method', type=str, default='tfidf',
                        choices=['tfidf', 'bow'],
                        help='Vectorization method')
    
    args = parser.parse_args()
    train_model(args.model, args.method)

