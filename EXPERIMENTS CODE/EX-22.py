"""
Exercise 22: Confidence Interval for Mean Customer Rating
Key Idea: the confidence interval is calculated around the sample mean rating.
"""

import pandas as pd
from scipy import stats

data = pd.read_csv("customer_reviews.csv")
ratings = data["rating"].dropna()

confidence = 0.95
mean = ratings.mean()
sem = stats.sem(ratings)
ci = stats.t.interval(
    confidence, len(ratings) - 1,
    loc=mean, scale=sem
)

print("Mean rating =", mean)
print("95% Confidence interval =", ci)
