"""
Exercise 11: Sales over Time - Line, Scatter and Bar Plots
Key Idea: combine line, scatter, and bar visualizations to represent sales progression over time.
"""

import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6]
sales = [100, 120, 150, 140, 180, 200]

plt.plot(months, sales, marker="o")
plt.title("Sales over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.scatter(months, sales)
plt.title("Sales - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
