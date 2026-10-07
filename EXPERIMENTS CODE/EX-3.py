"""
Exercise 3: Average Sale Price of Houses with More Than 4 Bedrooms
Key Idea: first filter rows, then select the sale-price column.
"""

import numpy as np

# Columns: Bedrooms, Area, Sale Price
house_data = np.array([
    [3, 1200, 250000],
    [5, 1800, 400000],
    [6, 2200, 500000],
    [4, 1500, 320000],
    [5, 2000, 450000]
])

selected = house_data[house_data[:, 0] > 4]
average_price = np.mean(selected[:, 2])
print("Average sale price =", average_price)
