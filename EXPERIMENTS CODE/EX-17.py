"""
Exercise 17: Customer Feedback - Top N Word Frequency
Key Idea: clean the text before counting words.
"""

import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
stop_words = {"the", "and", "is", "a", "an", "of", "to", "in"}

words = []
for text in data["feedback"].dropna():
    text = text.lower()
    words.extend(re.findall(r"\b[a-z]+\b", text))

words = [word for word in words if word not in stop_words]
frequency = Counter(words)

n = int(input("Enter N: "))
top_words = frequency.most_common(n)
print(top_words)

names = [x[0] for x in top_words]
counts = [x[1] for x in top_words]

plt.bar(names, counts)
plt.xticks(rotation=45)
plt.title("Top Words in Customer Feedback")
plt.show()
