from pandas import read_csv, crosstab
from numpy import argmin
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from scipy.stats import chi2_contingency


class ABTestAnalyzer:
    def __init__(self, file_path):
        """
        Initialize the ABTestAnalyzer object.
        
        Args:
        - file_path: Path to the CSV file containing the data
        """
        self.data = self.load_data(file_path)

        # Attributes for sample sizes
        self.n_control = len(self.data[self.data['group'] == 'control'])
        self.n_treatment = len(self.data[self.data['group'] == 'treatment'])
        self.n_max = min(self.n_control, self.n_treatment)

        # Constant for printing
        self.N_DASH = 40
    
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
        self.N_DASH = 40
        print("-" * self.N_DASH)
        print("Shape of DataFrame:")
        print(self.data.shape)
        print("-" * self.N_DASH)
        print("Column Names:")
        print(self.data.columns)
        print("-" * self.N_DASH)
        print("Unique Entries:")
        print(self.data.nunique())
        print("-" * self.N_DASH)
        print("Check for NA values:")
        print(self.data.isna().sum())
        print("-" * self.N_DASH)
        print("Number of Records in Control and Treatment Group:")
        print("Control Group:", self.n_control)
        print("Treatment Group:", self.n_treatment)
        print("-" * self.N_DASH)


    def run_ztest(self, N_sample=None):
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
        z_value, p_value = proportions_ztest([control_sample['converted'].sum(), treatment_sample['converted'].sum()], 
                                             [len(control_sample), len(treatment_sample)])
        
        # Print output
        print('-'*self.N_DASH)
        print("Control Conversion Rate:", control_conversion_rate)
        print("Treatment Conversion Rate:", treatment_conversion_rate)
        print("P-value for A/B test:", p_value)
        print('-'*self.N_DASH)

        return p_value
          
    def run_chisquare(self):
        """
        Perform A/B test using Chi-squared test for independence.
        
        Returns:
        - p_value: The p-value resulting from the Chi-squared test
        """
        # Create a contingency table
        contingency_table = crosstab(self.data['group'], self.data['converted'])
        
        # Perform Chi-squared test
        chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)
        
        # Print p-value
        print('-'*self.N_DASH)
        print("P-value for A/B test (Chi-squared test):", p_value)
        print("Chi2_stat: ", chi2_stat)
        print('-'*self.N_DASH)

        return p_value