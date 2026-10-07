"""
Exercise 18: Mean, Median, Standard Deviation, Boxplot, Scatter Plot and Q-Q Plot
Key Idea: Pandas calculates summary statistics; Matplotlib/SciPy create the plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.DataFrame({
    "Age": [20, 22, 25, 28, 30, 32, 35, 40],
    "Fat": [15, 18, 20, 22, 24, 27, 30, 32]
})

print("Mean:")
print(data.mean())

print("Median:")
print(data.median())

print("Standard deviation:")
print(data.std())

data[["Age", "Fat"]].boxplot()
plt.title("Boxplots")
plt.show()

plt.scatter(data["Age"], data["Fat"])
plt.xlabel("Age")
plt.ylabel("Body Fat")
plt.title("Age vs Body Fat")
plt.show()

stats.probplot(data["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()
