from pandas import read_csv
from numpy import argmin
from statsmodels.stats.proportion import proportions_ztest, proportion_confint


class ABTestAnalyzer:
    def __init__(self, file_path):
        """
        Initialize the ABTestAnalyzer object.
        
        Args:
        - file_path: Path to the CSV file containing the data
        """
        self.data = self.load_data(file_path)
        self.n_control = len(self.data[self.data['group'] == 'control'])
        self.n_treatment = len(self.data[self.data['group'] == 'treatment'])
        self.n_max = min(self.n_control, self.n_treatment)
    
    def load_data(self, file_path):
        """
        Load data from a CSV file into a DataFrame.
        
        Args:
        - file_path: Path to the CSV file
        
        Returns:
        - DataFrame: Pandas DataFrame containing the data
        """
        return read_csv(file_path)
    
    def drop_duplicates(self, col_name='user_id'):
        """
        Drop duplicate records based on a provided column (default: 'user_id')
        
        Returns:
        - DataFrame: DataFrame with duplicate records removed
        """

        self.data = self.data.drop_duplicates(subset=col_name)
        return self.data
    
    def print_data_info(self):
        """
        Print a general overview of the data.
        
        Returns:
        None
        """
        N_DASHES = 40
        print("-" * N_DASHES)
        print("Shape of DataFrame:")
        print(self.data.shape)
        print("-" * N_DASHES)
        print("Column Names:")
        print(self.data.columns)
        print("-" * N_DASHES)
        print("Unique Entries:")
        print(self.data.nunique())
        print("-" * N_DASHES)
        print("Check for NA values:")
        print(self.data.isna().sum())
        print("-" * N_DASHES)
        print("Number of Records in Control and Treatment Group:")
        print("Control Group:", self.n_control)
        print("Treatment Group:", self.n_treatment)
        print("-" * N_DASHES)


    def run_abtest(self, N_sample: None | int, alpha=0.05):
        """
        Perform A/B test given a sample size and alpha value.
        
        Args:
        - N_sample: Sample size for both control and treatment groups
        - alpha: Alpha value for the significance level (default is 0.05)
        
        Returns:
        - p_value: The p-value resulting from the A/B test
        """
        if N_sample is None:
            print(f'No sample size provided using maximum available ({self.n_max}).')
            N_sample = self.n_max
        elif N_sample > self.n_max:
            print(f'Sample size provided is too high. Using maximum available ({self.n_max}).')
            N_sample = self.n_max

        # Randomly sample control and treatment groups
        control_sample = self.data[self.data['group'] == 'control'].sample(n=N_sample, random_state=42)
        treatment_sample = self.data[self.data['group'] == 'treatment'].sample(n=N_sample, random_state=42)
        
        # Calculate individual conversion rates
        control_conversion_rate = control_sample['converted'].mean()
        treatment_conversion_rate = treatment_sample['converted'].mean()
        
        # Perform A/B test
        z_score, p_value = proportions_ztest([control_sample['converted'].sum(), treatment_sample['converted'].sum()], 
                                             [len(control_sample), len(treatment_sample)])
        
        # Print conversion rates
        print("Control Conversion Rate:", control_conversion_rate)
        print("Treatment Conversion Rate:", treatment_conversion_rate)
        
        # Print p-value
        print("P-value for A/B test:", p_value)
        
        return p_value