import pytest
import pandas as pd
import numpy as np
import os
import sys
from sklearn.utils.validation import check_is_fitted

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.assignment_3 import prepare_target, split_data, train_model, evaluate_model

@pytest.fixture
def ml_df():
    return pd.DataFrame({
        'Age': [20, 30, 40, 50, 60, 25, 35, 45, 55, 65],
        'TotalSpending': [100, 200, 300, 400, 500, 150, 250, 350, 450, 550],
        'Transported': [True, False, True, False, True, False, True, False, True, False]
    })

def test_prepare_target(ml_df):
    df = prepare_target(ml_df.copy())
    assert df['Transported'].dtype in [np.int64, np.int32]
    assert df['Transported'].iloc[0] == 1
    assert df['Transported'].iloc[1] == 0

def test_split_data(ml_df):
    features = ['Age', 'TotalSpending']
    target = 'Transported'
    X_train, X_test, y_train, y_test = split_data(ml_df, features, target, test_size=0.2, random_state=42)
    
    # 10 rows, 20% test = 2 rows test, 8 rows train
    assert len(X_train) == 8
    assert len(X_test) == 2
    assert len(y_train) == 8
    assert len(y_test) == 2

def test_train_model(ml_df):
    df = prepare_target(ml_df.copy())
    X = df[['Age', 'TotalSpending']]
    y = df['Transported']
    
    model = train_model(X, y)
    # Check if scikit-learn model is fitted
    check_is_fitted(model)
    assert hasattr(model, "predict")

def test_evaluate_model(ml_df):
    df = prepare_target(ml_df.copy())
    X = df[['Age', 'TotalSpending']]
    y = df['Transported']
    
    # Fake training on whole set just to test evaluation
    model = train_model(X, y)
    metrics = evaluate_model(model, X, y)
    
    assert 'accuracy' in metrics
    assert 'f1_score' in metrics
    assert 0 <= metrics['accuracy'] <= 1
    assert 0 <= metrics['f1_score'] <= 1
