"""
Exercise 21: Point Estimate and Confidence Interval from CSV
Key Idea: the sample mean is the point estimate; the confidence interval gives a range for the population mean.
"""

import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv("rare_elements.csv")
values = data.iloc[:, 0].dropna()

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (for example 0.95): "))
precision = float(input("Enter desired precision: "))

sample = values.sample(n=min(n, len(values)), random_state=1)
mean = sample.mean()
sem = stats.sem(sample)
ci = stats.t.interval(
    confidence, len(sample) - 1, loc=mean, scale=sem
)

print("Point estimate =", mean)
print("Confidence interval =", ci)
print("Desired precision =", precision)
