"""
Exercise 33: Multiple Linear Regression for Car Price
Key Idea: multiple regression uses several features to predict price.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.DataFrame({
    "Engine": [1.2, 1.5, 1.8, 2.0, 2.2, 2.5],
    "Horsepower": [80, 100, 120, 140, 160, 190],
    "Mileage": [20, 18, 16, 15, 13, 11],
    "Price": [8000, 10000, 13000, 16000, 19000, 23000]
})

X = data[["Engine", "Horsepower", "Mileage"]]
y = data["Price"]

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(X)
print("R-squared =", r2_score(y, predicted))
print("Coefficients =", model.coef_)

new_car = [[1.8, 120, 16]]
print("Predicted price =", model.predict(new_car)[0])
