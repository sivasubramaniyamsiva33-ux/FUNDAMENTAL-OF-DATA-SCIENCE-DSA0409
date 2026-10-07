import numpy as np

prices = np.array([
    [100, 120, 150],
    [80, 90, 110],
    [200, 180, 160]
])

average_price = np.mean(prices)

print("Average price =", average_price)
