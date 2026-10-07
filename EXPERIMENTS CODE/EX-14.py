"""
Exercise 14: Frequency Distribution of Customer Ages
Key Idea: value_counts() counts distinct age occurrences and sort_index() keeps bins in chronological order.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Age": [20, 25, 20, 30, 25, 20, 35, 30, 25]
})

frequency = data["Age"].value_counts().sort_index()
print(frequency)

frequency.plot(kind="bar")
plt.title("Customer Age Frequency")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
