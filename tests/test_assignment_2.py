import pytest
import pandas as pd
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.assignment_2 import calculate_total_spending, parse_cabin, filter_outliers_iqr

@pytest.fixture
def spending_df():
    return pd.DataFrame({
        'RoomService': [100.0, 200.0, np.nan],
        'FoodCourt': [50.0, np.nan, 150.0],
        'ShoppingMall': [0.0, 50.0, 50.0],
        'Spa': [np.nan, 10.0, 10.0],
        'VRDeck': [0.0, 0.0, 0.0]
    })

@pytest.fixture
def cabin_df():
    return pd.DataFrame({
        'Cabin': ['B/0/P', 'F/1/S', np.nan, 'G/10/P']
    })

def test_calculate_total_spending(spending_df):
    df = calculate_total_spending(spending_df.copy())
    assert 'TotalSpending' in df.columns
    # Row 0: 100+50+0+0+0 = 150
    # Row 1: 200+0+50+10+0 = 260
    # Row 2: 0+150+50+10+0 = 210
    assert df.loc[0, 'TotalSpending'] == 150.0
    assert df.loc[1, 'TotalSpending'] == 260.0
    assert df.loc[2, 'TotalSpending'] == 210.0

def test_parse_cabin(cabin_df):
    df = parse_cabin(cabin_df.copy())
    assert 'Deck' in df.columns
    assert 'CabinNum' in df.columns
    assert 'Side' in df.columns
    
    assert df.loc[0, 'Deck'] == 'B'
    assert df.loc[0, 'CabinNum'] == 0
    assert df.loc[0, 'Side'] == 'P'
    
    assert pd.isna(df.loc[2, 'Deck'])
    assert df.loc[3, 'CabinNum'] == 10

def test_filter_outliers_iqr():
    # Data: [10, 11, 12, 13, 14, 15, 100]
    # Q1 = 11.5, Q3 = 14.5, IQR = 3
    # Upper bound = 14.5 + 4.5 = 19
    df = pd.DataFrame({'val': [10, 11, 12, 13, 14, 15, 100]})
    filtered_df = filter_outliers_iqr(df, 'val')
    
    assert len(filtered_df) == 6
    assert 100 not in filtered_df['val'].values
    assert 15 in filtered_df['val'].values
