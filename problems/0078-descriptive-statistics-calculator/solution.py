import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    d = np.array(data)
    values, counts = np.unique(d, return_counts=True)
    mode = values[np.argmax(counts)]
    q25 = np.percentile(d, 25)
    q50 = np.percentile(d, 50)
    q75 = np.percentile(d, 75)
    return {'mean': np.mean(d), 'median': np.median(d), 'mode': mode, 'variance': np.var(d), 'standard_deviation': np.std(d), '25th_percentile': q25, '50th_percentile': q50, '75th_percentile': q75, 'interquartile_range': q75-q25}