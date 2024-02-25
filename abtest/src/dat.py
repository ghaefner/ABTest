import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
    - file_path: Path to the CSV file
    
    Returns:
    - DataFrame: Pandas DataFrame containing the data
    """
    return pd.read_csv(file_path)