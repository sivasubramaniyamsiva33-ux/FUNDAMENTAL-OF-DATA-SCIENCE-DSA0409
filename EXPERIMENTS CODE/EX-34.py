"""
Exercise 34: KNN Classification with Evaluation Metrics
Key Idea: evaluate the KNN classifier using standard classification metrics.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)

X = np.array([
    [20, 120], [22, 130], [25, 125], [27, 140],
    [40, 180], [42, 190], [45, 185], [48, 200]
])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy =", accuracy_score(y_test, y_pred))
print("Precision =", precision_score(y_test, y_pred))
print("Recall =", recall_score(y_test, y_pred))
print("F1-score =", f1_score(y_test, y_pred))

new_patient = [[30, 150]]
print("Prediction =", model.predict(new_patient))
