"""
Exercise 4: Total Yearly Sales and Percentage Increase
Key Idea: np.sum() gives total sales; percentage increase = (new-old)/old * 100.
"""

import numpy as np

sales_data = np.array([10000, 12000, 15000, 18000])

total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total sales =", total_sales)
print("Percentage increase =", percentage_increase, "%")
