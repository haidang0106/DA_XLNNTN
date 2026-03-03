# 📘 NLP Text & News Classification Project

## 1️⃣ Project Overview

**Course:** Xử lý Ngôn ngữ Tự nhiên (Natural Language Processing – NLP)  

**Topic:** Phân loại văn bản và tin tức (Text & News Classification)

**Goal:**  
Xây dựng hệ thống phân loại văn bản tự động dựa trên các thuật toán Machine Learning và/hoặc Deep Learning.

### Example Categories

- Chính trị  
- Kinh tế  
- Thể thao  
- Giải trí  
- Công nghệ  

### Dataset Options

- Vietnamese news dataset (VNExpress, Zing, etc.)
- Kaggle news classification datasets
- Custom collected dataset (phải ghi rõ nguồn)

---

## 2️⃣ Project Structure Guidelines

### Recommended Structure

```bash
nlp-text-classification/
│
├── data/
│   ├── raw/                  # Dữ liệu gốc
│   ├── processed/            # Dữ liệu sau tiền xử lý
│
├── notebooks/                # Jupyter Notebook thử nghiệm
│
├── src/
│   ├── preprocessing.py      # Tiền xử lý văn bản
│   ├── feature_engineering.py
│   ├── model.py              # Định nghĩa model
│   ├── train.py              # Huấn luyện
│   ├── evaluate.py           # Đánh giá
│   └── utils.py
│
├── models/                   # Lưu model đã train
│
├── reports/                  # Báo cáo, biểu đồ
│
├── requirements.txt
└── README.md
```

---

## 3️⃣ Dev Environment Tips

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

- Windows:
```bash
venv\Scripts\activate
```

- Mac/Linux:
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Common Libraries

- numpy  
- pandas  
- scikit-learn  
- matplotlib / seaborn  
- underthesea (Vietnamese NLP)  
- pyvi  
- torch hoặc tensorflow (Deep Learning)

### If Using Jupyter

```bash
pip install notebook
jupyter notebook
```

---

## 4️⃣ Data Preprocessing Instructions

### Must Implement

- Lowercasing
- Remove special characters
- Remove stopwords
- Tokenization

### Optional

- Lemmatization
- Stemming
- Word segmentation (for Vietnamese)

### Vectorization Methods

- Bag of Words (CountVectorizer)
- TF-IDF
- Word2Vec
- FastText
- BERT embeddings (optional advanced)

⚠ All preprocessing steps must be reproducible and documented clearly.

---

## 5️⃣ Model Development Instructions

### Baseline Models

- Naive Bayes
- Logistic Regression
- SVM
- Random Forest

### Advanced Models

- LSTM
- CNN for text
- PhoBERT / BERT

### Training Rules

- Split dataset: train / validation / test
- Use cross-validation when possible
- Save trained model to `/models`
- Log metrics clearly

---

## 6️⃣ Evaluation Instructions

### Must Report

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### Use

```python
sklearn.metrics.classification_report
sklearn.metrics.confusion_matrix
```

### Include Visualization

- Confusion matrix
- Loss curve (if deep learning)

### Compare At Least

- 1 traditional ML model
- 1 deep learning model (if applicable)

---

## 7️⃣ Experiment Tracking Rules

Always document:

- Dataset version
- Preprocessing version
- Model parameters
- Training time

📌 Keep a results table in `reports/`

⚠ Do not overwrite best model without backup.

⚠ Use consistent random seed for reproducibility.

---

## 8️⃣ Coding Rules

- Follow PEP8
- Write modular code (no giant notebooks-only project)
- Functions must have docstrings
- Avoid hard-coded paths
- Use relative paths

---

## 9️⃣ Testing Instructions

- Ensure preprocessing runs without errors on full dataset
- Ensure training script runs end-to-end

After modifying model or preprocessing:

- Re-run training
- Re-check metrics
- Verify model loading works correctly

If adding new feature:

- Compare performance before & after
- Document improvement

---

## 🔟 Report Requirements

The final report must include:

- Introduction
- Literature review (brief)
- Dataset description
- Methodology
- Experiments
- Results comparison
- Discussion
- Conclusion & Future work

Include:

- Tables
- Graphs
- Model comparison
- Error analysis

---

## 1️⃣1️⃣ PR / Submission Instructions

Final folder must include:

- Source code
- Trained model
- requirements.txt
- Report (PDF)

Before submission:

- Run full training pipeline
- Remove unused files
- Ensure reproducibility

✅ Another person must be able to clone repo and run successfully.
