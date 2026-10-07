"""
Exercise 38: Temperature Analysis for Different Cities
Key Idea: axis=1 calculates statistics across each city's daily readings.
"""

import numpy as np

# Rows = cities, columns = daily readings
temperatures = np.array([
    [25, 27, 30, 28, 26],
    [20, 21, 22, 21, 20],
    [30, 32, 35, 33, 31]
])

cities = ["Chennai", "Bengaluru", "Delhi"]

mean = np.mean(temperatures, axis=1)
std = np.std(temperatures, axis=1)
temperature_range = np.ptp(temperatures, axis=1)

for i in range(3):
    print(cities[i])
    print("Mean =", mean[i])
    print("Standard deviation =", std[i])
    print("Range =", temperature_range[i])

highest_range = np.argmax(temperature_range)
most_consistent = np.argmin(std)

print("Highest temperature range:", cities[highest_range])
print("Most consistent city:", cities[most_consistent])
