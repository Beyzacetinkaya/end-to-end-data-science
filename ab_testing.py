import numpy as np # type: ignore
from scipy import stats # type: ignore
group_A = np.random.binomial(1, 0.05, 1000)
group_B = np.random.binomial(1, 0.06, 1000)
t_stat, p_value = stats.ttest_ind(group_A, group_B)
print("p-value:", p_value)
if p_value < 0.05:
    print("Statistically significant difference.")
else:
    print("No significant difference.")