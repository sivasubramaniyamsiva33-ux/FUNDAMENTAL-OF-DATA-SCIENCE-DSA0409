"""
Exercise 8: Top 5 Products Sold
Key Idea: groupby + sum + sort_values + head(5) finds the top products.
"""

import pandas as pd

sales = pd.DataFrame({
    "Product": ["Pen", "Book", "Pen", "Bag", "Book", "Pen", "Bag"],
    "Quantity": [10, 8, 15, 5, 12, 20, 9]
})

top5 = sales.groupby("Product")["Quantity"].sum()
top5 = top5.sort_values(ascending=False).head(5)
print(top5)
