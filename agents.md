# AGENTS.md – NLP Text & News Classification

## Project Overview

Course: Natural Language Processing (NLP)  
Topic: Text & News Classification  

Goal: Build an automated text classification system using Machine Learning and/or Deep Learning.

Target labels:

- Chính trị
- Kinh tế
- Thể thao
- Giải trí
- Công nghệ

---

## Repository Structure

```
nlp-text-classification/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
│
├── models/
├── reports/
├── requirements.txt
└── README.md
```

Do not modify structure unless necessary.  
All scripts must run using relative paths.

---

## Dev Environment

Create virtual environment:

```
python -m venv venv
```

Activate:

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Core libraries:

- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- underthesea / pyvi
- torch or tensorflow (if deep learning)

If using Jupyter:

```
pip install notebook
jupyter notebook
```

---

## Data Preprocessing Rules

Must implement:

- Lowercasing
- Remove special characters
- Remove stopwords
- Tokenization

Optional:

- Lemmatization
- Stemming
- Vietnamese word segmentation

Vectorization options:

- CountVectorizer
- TF-IDF
- Word2Vec
- FastText
- BERT embeddings

All preprocessing must be:

- Reproducible
- Versioned
- Fully documented

---

## Model Development

Baseline models:

- Naive Bayes
- Logistic Regression
- SVM
- Random Forest

Advanced models:

- LSTM
- CNN for text
- PhoBERT / BERT

Training requirements:

- Train / validation / test split
- Use cross-validation when possible
- Fix random seed
- Save models to `/models`
- Log training time
- Log hyperparameters

Never overwrite best model without backup.

---

## Evaluation Requirements

Must report:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Use:

```
sklearn.metrics.classification_report
sklearn.metrics.confusion_matrix
```

Include:

- Confusion matrix visualization
- Loss curve (if deep learning)

Must compare:

- At least 1 traditional ML model
- At least 1 deep learning model (if applicable)

---

## Experiment Tracking

For every experiment, record:

- Dataset version
- Preprocessing version
- Model parameters
- Training time
- Metrics

Maintain a results table in `/reports`.

Do not delete historical experiment results.

---

## Coding Standards

- Follow PEP8
- Modular design (no notebook-only implementation)
- Use docstrings
- Avoid hard-coded paths
- Use relative imports
- Separate preprocessing, training, evaluation logic

---

## Testing Rules

Before submission:

- Preprocessing must run on full dataset without error
- Training script must run end-to-end
- Model loading must work correctly
- Metrics must be reproducible

If modifying:

- Re-train model
- Re-evaluate metrics
- Document performance difference

---

## Report Requirements

Final report must include:

- Introduction
- Literature review
- Dataset description
- Methodology
- Experiments
- Results comparison
- Discussion
- Conclusion
- Future work

Include tables, graphs, comparison charts, and error analysis.

---

## Submission Checklist

Final submission must include:

- Source code
- Trained model
- requirements.txt
- Final PDF report

Before submitting:

- Run full pipeline
- Remove unused files
- Ensure reproducibility

Another person must be able to clone the repository and run successfully without modification.
