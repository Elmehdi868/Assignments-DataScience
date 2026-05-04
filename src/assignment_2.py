import pandas as pd
import numpy as np

def calculate_total_spending(df):
    """
    Create a new column 'TotalSpending' by summing up:
    'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', and 'VRDeck'.
    Handle missing values by treating them as 0 before summing.
    Should return the modified DataFrame.
    """
    # TODO: Implement this function
    pass

def parse_cabin(df):
    """
    The 'Cabin' column is in the format 'Deck/Num/Side' (e.g., 'B/0/P').
    Split this into three new columns: 'Deck', 'CabinNum', and 'Side'.
    If 'Cabin' is NaN, these new columns should also be NaN.
    'CabinNum' should be converted to numeric (float or int).
    Should return the modified DataFrame.
    """
    # TODO: Implement this function
    pass

def filter_outliers_iqr(df, column_name):
    """
    Identify and remove outliers in the specified column using the IQR method.
    - Calculate Q1 (25th percentile) and Q3 (75th percentile).
    - Calculate IQR = Q3 - Q1.
    - Define bounds: Lower = Q1 - 1.5 * IQR, Upper = Q3 + 1.5 * IQR.
    - Keep only rows where the column value is within [Lower, Upper].
    Should return the filtered DataFrame.
    """
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    # Test your logic here
    try:
        # Assuming assignment_1.py functions are used or mock data is loaded
        print("Assignment 2 template ready for implementation.")
    except Exception as e:
        print(f"Error: {e}")
