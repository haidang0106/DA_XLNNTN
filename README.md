# 📰 NLP Text & News Classification
> Natural Language Processing Project – Text & News Categorization

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Overview

This project builds an automated **text and news classification system** using both **Traditional Machine Learning** and **Deep Learning** approaches.

The system classifies news articles into predefined categories such as:

- Chính trị (Politics)
- Kinh tế (Economics)
- Thể thao (Sports)
- Giải trí (Entertainment)
- Công nghệ (Technology)

---

## 🎯 Objectives

- Implement a full NLP pipeline from preprocessing → feature engineering → model training → evaluation
- Compare performance between:
  - Traditional ML models
  - Deep Learning models
- Ensure reproducibility and modular code structure


---

## 📊 Dataset

Possible dataset sources:

- Vietnamese news datasets (VNExpress, Zing, etc.)
- Kaggle News Classification datasets
- Custom collected dataset (with documented source)

### Data Split

- Train set
- Validation set
- Test set

Random seed is fixed for reproducibility.



## 📈 Evaluation Metrics

The following metrics are reported:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Using:

```python
sklearn.metrics.classification_report
sklearn.metrics.confusion_matrix
```

Additional Visualizations:

- Confusion Matrix Heatmap
- Loss Curve (Deep Learning models)

---

## 🧪 Experiment Tracking

Each experiment documents:

- Dataset version
- Preprocessing version
- Model hyperparameters
- Training time
- Performance metrics

Results are summarized in `/reports`.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/haidang0106/nlp-text-classification.git
cd nlp-text-classification
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

- Windows:
```bash
venv\Scripts\activate
```

- Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Preprocessing

```bash
python src/preprocessing.py
```

### Training

```bash
python src/train.py
```

### Evaluation

```bash
python src/evaluate.py
```

---

## 📊 Results Summary

| Model | Accuracy | F1-Score | Notes |
|--------|----------|----------|--------|
| Logistic Regression | xx% | xx% | Baseline |
| SVM | xx% | xx% | Strong performance |
| LSTM | xx% | xx% | Deep learning |
| PhoBERT | xx% | xx% | Best performance |

---

## 🧠 Key Learnings

- Importance of text preprocessing in Vietnamese NLP
- TF-IDF vs Embeddings performance comparison
- Deep Learning improves performance with sufficient data
- Model evaluation beyond accuracy (F1-score & confusion matrix)

---

## 📄 Report

Final report includes:

- Introduction
- Literature review
- Dataset description
- Methodology
- Experiments
- Results comparison
- Error analysis
- Conclusion & Future work

---

## 🔐 Reproducibility

- Fixed random seed
- Modular code structure
- No hard-coded paths
- Fully runnable pipeline

Another user can clone the repo and reproduce results successfully.

---

## 👨‍💻 Author

Student Project – Natural Language Processing Course  
University Assignment – 2026

---

## 📜 License

This project is for educational purposes.
