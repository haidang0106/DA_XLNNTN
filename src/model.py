from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def get_model(model_name='naive_bayes'):
    """
    Trả về một mô hình (estimator) tương ứng với tên.
    """
    if model_name == 'naive_bayes':
        return MultinomialNB()
    elif model_name == 'logistic_regression':
        return LogisticRegression(max_iter=1000)
    elif model_name == 'svm':
        return SVC(kernel='linear', probability=True)
    elif model_name == 'random_forest':
        return RandomForestClassifier(n_estimators=100)
    else:
        raise ValueError(f"Model {model_name} not supported.")

