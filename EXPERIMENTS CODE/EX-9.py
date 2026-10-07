"""
Exercise 9: Property Data Analysis using Pandas
Key Idea: groupby(), conditions and idxmax() solve the three tasks.
"""

import pandas as pd

property_data = pd.DataFrame({
    "Location": ["Chennai", "Chennai", "Madurai", "Madurai", "Chennai"],
    "Bedrooms": [3, 5, 4, 6, 5],
    "Area": [1200, 1800, 1500, 2200, 2000],
    "Price": [300000, 450000, 350000, 500000, 480000]
})

print("Average price by location:")
print(property_data.groupby("Location")["Price"].mean())

print("Properties with more than 4 bedrooms:")
print((property_data["Bedrooms"] > 4).sum())

largest = property_data.loc[property_data["Area"].idxmax()]
print("Property with largest area:")
print(largest)
