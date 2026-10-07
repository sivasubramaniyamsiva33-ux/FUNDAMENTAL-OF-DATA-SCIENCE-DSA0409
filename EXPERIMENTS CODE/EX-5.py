"""
Exercise 5: Average Fuel Efficiency and Percentage Improvement
Key Idea: percentage improvement compares the new value with the old value.
"""

import numpy as np

fuel_efficiency = np.array([25, 30, 28, 35, 32])

average = np.mean(fuel_efficiency)
old_model = fuel_efficiency[0]
new_model = fuel_efficiency[1]

improvement = ((new_model - old_model) / old_model) * 100

print("Average fuel efficiency =", average)
print("Percentage improvement =", improvement, "%")
