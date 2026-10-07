"""
Exercise 12: Monthly Temperature and Rainfall Plots
Key Idea: visualize paired climate parameters with separate plots.
"""

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temperature = [25, 27, 29, 31, 32, 30]
rainfall = [20, 15, 30, 80, 120, 100]

plt.plot(months, temperature, marker="o")
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.show()

plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.show()
