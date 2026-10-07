"""
Exercise 32: Bivariate Analysis and Linear Regression for House Price
Key Idea: bivariate analysis examines two variables; regression models their relationship.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.DataFrame({
    "Size": [800, 1000, 1200, 1500, 1800, 2000],
    "Price": [160, 200, 240, 300, 360, 400]
})

X = data[["Size"]]
y = data["Price"]

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(X)
print("R-squared =", r2_score(y, predicted))

plt.scatter(data["Size"], data["Price"])
plt.plot(data["Size"], predicted)
plt.xlabel("House Size")
plt.ylabel("Price")
plt.title("House Size vs Price")
plt.show()

new_size = float(input("Enter house size: "))
print("Predicted price =", model.predict([[new_size]])[0])
