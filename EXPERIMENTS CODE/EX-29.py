"""
Exercise 29: Accuracy, Precision, Recall and F1-Score
Key Idea: accuracy, precision, recall and F1-score compare actual and predicted labels.
"""

from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)

# Actual and predicted values
y_test = [0, 1, 1, 0, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 0, 1, 0]

print("Accuracy =", accuracy_score(y_test, y_pred))
print("Precision =", precision_score(y_test, y_pred))
print("Recall =", recall_score(y_test, y_pred))
print("F1-score =", f1_score(y_test, y_pred))
