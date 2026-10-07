"""
Exercise 23: Hypothesis Testing for Treatment vs Placebo
Key Idea: hypothesis testing uses a test statistic and p-value.
"""

import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

control = np.array([5, 6, 7, 5, 6, 4, 7])
treatment = np.array([8, 9, 10, 9, 11, 8, 10])

t_stat, p_value = ttest_ind(treatment, control)
print("t-statistic =", t_stat)
print("p-value =", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("No significant difference")

plt.boxplot([control, treatment], labels=["Control", "Treatment"])
plt.title("Treatment vs Control")
plt.show()
