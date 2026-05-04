import pytest
import pandas as pd
import numpy as np
import os
import sys

# Add project root to path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.assignment_1 import load_data, clean_age, convert_types

@pytest.fixture
def mock_df():
    return pd.DataFrame({
        'PassengerId': ['0001_01', '0002_01', '0003_01', '0004_01'],
        'Age': [24.0, np.nan, 33.0, 40.0],
        'CryoSleep': [False, True, np.nan, 'False'],
        'VIP': [False, np.nan, False, 'True'],
        'Transported': [False, True, False, True]
    })

def test_load_data(tmp_path, mock_df):
    d = tmp_path / "data"
    d.mkdir()
    file_path = d / "train_mock.csv"
    mock_df.to_csv(file_path, index=False)
    
    loaded_df = load_data(str(file_path))
    assert isinstance(loaded_df, pd.DataFrame)
    assert len(loaded_df) == 4

def test_clean_age(mock_df):
    cleaned_df = clean_age(mock_df.copy())
    # Median of [24, 33, 40] is 33.0
    assert cleaned_df['Age'].isnull().sum() == 0
    assert cleaned_df.loc[1, 'Age'] == 33.0

def test_convert_types(mock_df):
    cleaned_df = convert_types(mock_df.copy())
    assert cleaned_df['CryoSleep'].dtype == bool
    assert cleaned_df['VIP'].dtype == bool
    # Test filling NaN with False
    assert cleaned_df.loc[2, 'CryoSleep'] == False
    assert cleaned_df.loc[1, 'VIP'] == False
