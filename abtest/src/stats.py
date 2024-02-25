import scipy.stats as stats
import statsmodels.stats.api as sms
from math import ceil

def power_analysis(base_conversion_rate: float, minimal_effect: float, stat_power=0.8, alpha=0.05) -> int:
    """
    Power analysis to calculate the minimum required sample size to measure a specific effect.
        
    Returns:
        required_sample_size: result from the power analysis rounded up to the next integer.
    """
    effect_size = sms.proportion_effectsize(prop1=base_conversion_rate,
                                            prop2=base_conversion_rate+minimal_effect)
    required_sample_size = sms.NormalIndPower().solve_power(effect_size, 
                                                            power=stat_power, 
                                                            alpha=alpha, 
                                                            ratio=1)
    print("-"*40)
    print(f'Required Sample Size: {ceil(required_sample_size)}.')
    print("-"*40)
    
    return ceil(required_sample_size)