AGENTS.md
Project overview

Course: Xử lý Ngôn ngữ Tự nhiên (Natural Language Processing – NLP)

Topic: Phân loại văn bản và tin tức (Text & News Classification)

Goal: Xây dựng hệ thống phân loại văn bản tự động dựa trên các thuật toán Machine Learning và/hoặc Deep Learning.

Example categories:

Chính trị

Kinh tế

Thể thao

Giải trí

Công nghệ

Dataset can be:

Vietnamese news dataset (VNExpress, Zing, etc.)

Kaggle news classification datasets

Custom collected dataset (must document source clearly)

Project structure guidelines

Recommended structure:

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
Dev environment tips

Use python -m venv venv to create virtual environment.

Activate environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Common libraries:

numpy

pandas

scikit-learn

matplotlib / seaborn

underthesea (for Vietnamese NLP)

pyvi

torch or tensorflow (if using deep learning)

If using Jupyter:

pip install notebook
jupyter notebook
Data preprocessing instructions

Must implement:

Lowercasing

Remove special characters

Remove stopwords

Tokenization

Optional:

Lemmatization

Stemming

Word segmentation (for Vietnamese)

Vectorization methods:

Bag of Words (CountVectorizer)

TF-IDF

Word2Vec

FastText

BERT embeddings (optional advanced)

All preprocessing steps must be reproducible and documented clearly.

Model development instructions

Baseline models:

Naive Bayes

Logistic Regression

SVM

Random Forest

Advanced models:

LSTM

CNN for text

PhoBERT / BERT

Training rules:

Split dataset: train / validation / test

Use cross-validation when possible

Save trained model to /models

Log metrics clearly

Evaluation instructions

Must report:

Accuracy

Precision

Recall

F1-score

Confusion Matrix

Use:

sklearn.metrics.classification_report
sklearn.metrics.confusion_matrix

Include visualization of:

Confusion matrix

Loss curve (if deep learning)

Compare at least:

1 traditional ML model

1 deep learning model (if applicable)

Experiment tracking rules

Always document:

Dataset version

Preprocessing version

Model parameters

Training time

Keep a results table in reports/.

Do not overwrite best model without backup.

Use consistent random seed for reproducibility.

Coding rules

Follow PEP8.

Write modular code (no giant notebooks-only project).

Functions must have docstrings.

Avoid hard-coded paths.

Use relative paths.

Testing instructions

Ensure preprocessing runs without errors on full dataset.

Ensure training script runs end-to-end.

After modifying model or preprocessing:

Re-run training.

Re-check metrics.

Verify model loading works correctly.

If adding new feature:

Compare performance before & after.

Document improvement.

Report requirements

The final report must include:

Introduction

Literature review (brief)

Dataset description

Methodology

Experiments

Results comparison

Discussion

Conclusion & Future work

Include:

Tables

Graphs

Model comparison

Error analysis

PR / Submission instructions

Final folder must include:

Source code

Trained model

requirements.txt

Report (PDF)

Run full training pipeline before submission.

Remove unused files.

Ensure reproducibility:

Another person must be able to clone repo and run successfully.