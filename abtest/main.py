from src.analyzer import ABTestAnalyzer


analyzer = ABTestAnalyzer(file_path="abtest/data/ab_data.csv")

analyzer.print_data_info()
analyzer.run_all(N_sample=4000)