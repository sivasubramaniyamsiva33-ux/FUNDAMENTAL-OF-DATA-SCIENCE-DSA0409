"""
Exercise 26: Linear Regression for Housing Price Prediction
Key Idea: linear regression learns the relationship between house area and price.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Area in square feet
X = np.array([[1000], [1200], [1500], [1800], [2000]])
# House prices
y = np.array([200000, 240000, 300000, 360000, 400000])

model = LinearRegression()
model.fit(X, y)

area = float(input("Enter house area: "))
prediction = model.predict([[area]])
print("Predicted house price =", prediction[0])
