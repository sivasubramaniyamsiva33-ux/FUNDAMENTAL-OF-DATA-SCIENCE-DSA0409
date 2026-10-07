"""
Exercise 37: Correlation between Study Time and Exam Score
Key Idea: correlation measures the strength/direction of linear association.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7],
    "Score": [45, 50, 58, 65, 72, 80, 88]
})

correlation = data["Study_Hours"].corr(data["Score"])
print("Correlation =", correlation)

plt.scatter(data["Study_Hours"], data["Score"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.show()
