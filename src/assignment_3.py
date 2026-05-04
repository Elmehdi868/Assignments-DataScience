import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

def prepare_target(df):
    """
    Convert the 'Transported' column from Boolean (True/False) to Integer (1/0).
    Should return the modified DataFrame.
    """
    # TODO: Implement this function
    pass

def split_data(df, features, target, test_size=0.2, random_state=42):
    """
    Split the data into training and testing sets.
    - features: List of column names to use as features.
    - target: The name of the target column.
    - test_size: Proportion of the dataset to include in the test split.
    - random_state: Pass an int for reproducible output.
    Returns: X_train, X_test, y_train, y_test
    """
    # TODO: Implement this function
    pass

def train_model(X_train, y_train):
    """
    Initialize and train a DecisionTreeClassifier on the training data.
    Return the trained model.
    """
    # TODO: Implement this function
    pass

def evaluate_model(model, X_test, y_test):
    """
    Predict the labels for the test set and calculate metrics.
    Returns a dictionary with 'accuracy' and 'f1_score'.
    """
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    print("Assignment 3 template ready.")
