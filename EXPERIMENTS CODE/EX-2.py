"""
Exercise 2: Average Product Price using NumPy
Key Idea: np.mean() calculates the average of all values in the array.
"""

import numpy as np

prices = np.array([
    [100, 120, 150],
    [80, 90, 110],
    [200, 180, 160]
])

average_price = np.mean(prices)
print("Average price =", average_price)
