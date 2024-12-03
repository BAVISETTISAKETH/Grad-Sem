# src/data_processing.py
import pandas as pd

def load_dataset(file_path):
    """Load a dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path, low_memory=False)
        print(f"Loaded data from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
