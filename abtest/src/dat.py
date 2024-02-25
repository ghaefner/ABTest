from pandas import read_csv

class ABTestAnalyzer:
    def __init__(self, file_path):
        """
        Initialize the ABTestAnalyzer object.
        
        Args:
        - file_path: Path to the CSV file containing the data
        """
        self.data = self.load_data(file_path)
    
    def load_data(self, file_path):
        """
        Load data from a CSV file into a DataFrame.
        
        Args:
        - file_path: Path to the CSV file
        
        Returns:
        - DataFrame: Pandas DataFrame containing the data
        """
        return read_csv(file_path)
    
    def print_data_info(self):
        """
        Print a general overview of the data.
        
        Returns:
        None
        """
        print("-" * 20)
        print("Shape of DataFrame:")
        print(self.data.shape)
        print("-" * 20)
        print("Column Names:")
        print(self.data.columns)
        print("-" * 20)
        print("Check for NA values:")
        print(self.data.isna().sum())
        print("-" * 20)
        print("Number of Records in Control and Treatment Group:")
        print("Control Group:", len(self.data[self.data['group'] == 'control']))
        print("Treatment Group:", len(self.data[self.data['group'] == 'treatment']))
        print("-" * 20)