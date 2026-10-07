"""
Exercise 24: KNN Classifier for a New Patient
Key Idea: KNN predicts a class using nearby training observations.
"""

from sklearn.neighbors import KNeighborsClassifier

# Features: symptom1, symptom2
X = [
    [1, 1], [1, 2], [2, 1],
    [8, 8], [9, 8], [8, 9]
]

# 0 = No condition, 1 = Condition
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

patient = [[7, 8]]
prediction = model.predict(patient)

if prediction[0] == 1:
    print("Patient may have the condition")
else:
    print("Patient may not have the condition")
