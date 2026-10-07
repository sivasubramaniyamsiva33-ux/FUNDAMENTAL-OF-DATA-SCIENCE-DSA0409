"""
Exercise 30: CART Regression for Used Car Price
Key Idea: DecisionTreeRegressor predicts a continuous value such as car price.
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Features: mileage, age
X = np.array([
    [20000, 2], [30000, 3], [40000, 4],
    [60000, 5], [80000, 7], [100000, 9]
])

price = np.array([18000, 17000, 15000, 13000, 10000, 7000])

model = DecisionTreeRegressor(max_depth=3, random_state=1)
model.fit(X, price)

mileage = float(input("Mileage: "))
age = float(input("Age: "))

prediction = model.predict([[mileage, age]])
print("Predicted price =", prediction[0])
