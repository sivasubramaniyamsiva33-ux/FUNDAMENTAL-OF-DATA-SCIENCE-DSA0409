"""
Exercise 15: Frequency Distribution of Likes
Key Idea: value_counts() calculates frequencies of post likes, plotted on a discrete bar chart.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Likes": [10, 20, 10, 30, 20, 10, 40, 30]
})

frequency = data["Likes"].value_counts().sort_index()
print(frequency)

frequency.plot(kind="bar")
plt.title("Frequency of Likes")
plt.xlabel("Likes")
plt.ylabel("Number of Posts")
plt.show()
