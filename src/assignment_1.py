import pandas as pd
import numpy as np


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the CSV file using pandas.
    Return the loaded DataFrame.
    """
    return pd.read_csv(file_path)


def clean_age(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in the 'Age' column by filling them with the median age.
    Should return the modified DataFrame.
    """
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age)
    return df


def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'CryoSleep' and 'VIP' columns to boolean types.
    Missing values in these columns should be treated as False before conversion.
    Should return the modified DataFrame.
    """
    
    truth_map = {
        True: True, "True": True, "true": True,
        False: False, "False": False, "false": False,
    }
    for col in ["CryoSleep", "VIP"]:
        df[col] = df[col].map(truth_map).fillna(False).astype(bool)
    return df


if __name__ == "__main__":
    # This block allows students to test their code locally
    try:
        data = load_data("data/train.csv")
        data = clean_age(data)
        data = convert_types(data)
        print("Basic cleaning successful!")
        print(data.head())
    except Exception as e:
        print(f"Error during execution: {e}")