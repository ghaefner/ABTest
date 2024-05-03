## A/B Testing Module

This Python module, ABTestAnalyzer, facilitates A/B testing analysis using different statistical methods. The module is designed to load data from a CSV file, perform data preprocessing, and execute various A/B testing procedures to compare control and treatment groups.

## Files Overview
src files:
- analyzer.py: Contains the ABTestAnalyzer class responsible for data loading, preprocessing, and conducting A/B tests.
- stats.py: Module for basic statistical calculations used within the ABTestAnalyzer.
run file:
- main.py: Demonstrates how to use the ABTestAnalyzer class to perform A/B testing on given data.

## Requirements
- Python 3.x
- pandas
- numpy
- statsmodels
- scipy

## Usage

1. Initialization
```python
from abtest.src.analyzer import ABTestAnalyzer

analyzer = ABTestAnalyzer(file_path="path/to/your/data.csv")
```

2. Data overview
To print an overview of the loaded data:
```python
analyzer.print_data_info()
```

3. Data preprocessing
Remove Duplicates:To remove duplicate records based on a specified column (default: 'user_id'):
```python
analyzer.drop_duplicates(col_name='user_id')
```

4. Perform A/B Testing
Run All Tests:To run all supported A/B tests (z-test, chi-squared test, Mann-Whitney U test):
```python
analyzer.run_all(N_sample=4000)
```

Or individual tests:
```python
analyzer.run_ztest(N_sample=4000)
```


## Class Methods
### Initialization:
- __init__(file_path): Initialize the ABTestAnalyzer object with data loaded from a CSV file.

### Data Preprocessing:
- load_data(file_path): Load data from a CSV file into a DataFrame.
- drop_duplicates(col_name='user_id'): Remove duplicate records based on a specified column.

### Data Overview:
- print_data_info(): Print a general overview of the loaded data.

### A/B Testing Methods:
- run_ztest(N_sample=None): Perform A/B test using z-test.
- run_chisquare(): Perform A/B test using Chi-squared test.
- run_utest(N_sample=None): Perform A/B test using Mann-Whitney U test.
- run_all(N_sample=None): Run all supported A/B tests and print the results.

## Example Usage
```python
from abtest.src.analyzer import ABTestAnalyzer

# Initialize ABTestAnalyzer with the data file path
analyzer = ABTestAnalyzer(file_path="path/to/your/data.csv")

# Print data overview
analyzer.print_data_info()

# Perform all A/B tests with a specified sample size
analyzer.run_all(N_sample=4000)

```

## Notes
- Ensure the CSV file specified in file_path contains relevant columns (group, converted, etc.) for A/B testing analysis.
- Modify the sample size (N_sample) according to your dataset size and testing requirements.