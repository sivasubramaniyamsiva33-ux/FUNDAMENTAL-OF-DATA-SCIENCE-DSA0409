"""
Exercise 16: Word Frequency in Customer Reviews
Key Idea: tokenizes review texts with regular expressions and tallies word frequencies across all reviews.
"""

import pandas as pd
import re
from collections import Counter

reviews = pd.DataFrame({
    "Review": [
        "good product and good service",
        "excellent product",
        "good quality product"
    ]
})

words = []
for review in reviews["Review"]:
    words.extend(re.findall(r"\b\w+\b", review.lower()))

frequency = Counter(words)
for word, count in frequency.most_common():
    print(word, ":", count)
