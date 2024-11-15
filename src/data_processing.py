# src/data_processing.py
import pandas as pd

def load_dataset(file_path):
    """Load dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
