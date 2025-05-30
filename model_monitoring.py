import numpy as np
def calculate_psi(expected, actual, buckets=10):
    expected_percents = np.histogram(expected, bins=buckets)[0] / len(expected)
    actual_percents = np.histogram(actual, bins=buckets)[0] / len(actual)
    psi = np.sum((expected_percents - actual_percents) * np.log(expected_percents / actual_percents + 1e-9))
    return psi
baseline = np.random.normal(0, 1, 1000)
current = np.random.normal(0.2, 1, 1000)
print("PSI:", calculate_psi(baseline, current))