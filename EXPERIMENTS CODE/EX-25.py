"""
Exercise 25: Decision Tree for Iris Classification
Key Idea: the trained decision tree predicts the Iris species from four measurements.
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target

model = DecisionTreeClassifier(random_state=1)
model.fit(X, y)

sepal_length = float(input("Sepal length: "))
sepal_width = float(input("Sepal width: "))
petal_length = float(input("Petal length: "))
petal_width = float(input("Petal width: "))

new_flower = [[
    sepal_length, sepal_width,
    petal_length, petal_width
]]

prediction = model.predict(new_flower)
print("Predicted species:", iris.target_names[prediction[0]])
