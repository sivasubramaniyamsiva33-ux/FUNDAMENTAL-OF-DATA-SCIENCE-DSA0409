"""
Exercise 7: Pandas Order Analysis
Key Idea: groupby() is useful for customer/product summaries.
"""

import pandas as pd

order_data = pd.DataFrame({
    "Customer_ID": [1, 1, 2, 2, 3],
    "Order_Date": ["2026-01-02", "2026-01-05", "2026-01-03", "2026-01-10", "2026-01-08"],
    "Product": ["Pen", "Book", "Pen", "Bag", "Book"],
    "Quantity": [2, 3, 5, 1, 4]
})

print("Orders by customer:")
print(order_data.groupby("Customer_ID").size())

print("Average quantity by product:")
print(order_data.groupby("Product")["Quantity"].mean())

order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])
print("Earliest date:", order_data["Order_Date"].min())
print("Latest date:", order_data["Order_Date"].max())
