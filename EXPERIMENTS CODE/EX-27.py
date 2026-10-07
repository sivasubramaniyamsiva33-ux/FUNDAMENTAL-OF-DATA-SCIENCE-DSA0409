"""
Exercise 27: Logistic Regression for Customer Churn
Key Idea: logistic regression predicts a binary outcome such as churn/not churn.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression

# Features: usage minutes, contract months
X = np.array([
    [100, 24], [120, 24], [80, 12],
    [300, 6], [280, 6], [350, 3]
])

# 0 = Not churned, 1 = Churned
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

usage = float(input("Usage minutes: "))
contract = float(input("Contract duration: "))

prediction = model.predict([[usage, contract]])
if prediction[0] == 1:
    print("Customer may churn")
else:
    print("Customer may not churn")
