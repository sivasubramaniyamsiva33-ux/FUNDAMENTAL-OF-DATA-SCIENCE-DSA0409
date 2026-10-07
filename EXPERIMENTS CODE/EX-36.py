"""
Exercise 36: Stock Price Variability from CSV
Key Idea: standard deviation and range describe variability.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("stock_data.csv")
prices = data["Close"]

print("Mean =", prices.mean())
print("Standard deviation =", prices.std())
print("Minimum =", prices.min())
print("Maximum =", prices.max())
print("Range =", prices.max() - prices.min())

plt.plot(prices)
plt.title("Stock Closing Prices")
plt.xlabel("Trading Day")
plt.ylabel("Closing Price")
plt.show()
