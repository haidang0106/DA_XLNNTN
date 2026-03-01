import os
import argparse
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluate_model(model_name, method='tfidf'):
    models_dir = "models"
    reports_dir = "reports"
    processed_path = os.path.join("data", "processed", "vietnamese_news_cleaned.csv")
    
    # 1. Load Data
    print(f"Loading data from {processed_path}...")
    df = pd.read_csv(processed_path)
    df = df.dropna(subset=['clean_text'])
    X_text = df['clean_text'].values
    y_true = df['label'].values
    
    # Lấy danh sách các nhãn độc nhất để vẽ plot
    classes = np.unique(y_true)
    
    # 2. Load Vectorizer
    vectorizer_path = os.path.join(models_dir, f"{method}_vectorizer.pkl")
    print(f"Loading vectorizer from {vectorizer_path}...")
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
        
    X_features = vectorizer.transform(X_text)
    
    # 3. Load Model
    model_path = os.path.join(models_dir, f"{model_name}_{method}.pkl")
    print(f"Loading model from {model_path}...")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    # 4. Predict
    print("Predicting...")
    y_pred = model.predict(X_features)
    
    # 5. Evaluate
    acc = accuracy_score(y_true, y_pred)
    print(f"\nModel: {model_name} | Method: {method}")
    print(f"Accuracy: {acc:.4f}\n")
    
    # 6. Classification Report
    report = classification_report(y_true, y_pred, target_names=classes)
    print("Classification Report:")
    print(report)
    
    # Save Report to file
    os.makedirs(reports_dir, exist_ok=True)
    report_path = os.path.join(reports_dir, f"{model_name}_{method}_report.txt")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"Model: {model_name} | Method: {method}\n")
        f.write(f"Accuracy: {acc:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write(report)
    print(f"Report saved to {report_path}")

    # 7. Confusion Matrix
    cm = confusion_matrix(y_true, y_pred, labels=classes)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=classes, yticklabels=classes)
    plt.title(f'Confusion Matrix: {model_name} ({method})')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    
    # Save Plot
    plot_path = os.path.join(reports_dir, f"{model_name}_{method}_cm.png")
    plt.savefig(plot_path, dpi=300)
    print(f"Confusion Matrix plot saved to {plot_path}")
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate NLP Classification Model")
    parser.add_argument('--model', type=str, default='naive_bayes', 
                        choices=['naive_bayes', 'logistic_regression', 'svm', 'random_forest'],
                        help='Name of the model to evaluate')
    parser.add_argument('--method', type=str, default='tfidf',
                        choices=['tfidf', 'bow'],
                        help='Vectorization method')
    
    args = parser.parse_args()
    evaluate_model(args.model, args.method)

