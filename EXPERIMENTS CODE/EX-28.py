"""
Exercise 28: K-Means Customer Segmentation
Key Idea: K-Means assigns observations to clusters based on feature similarity.
"""

import numpy as np
from sklearn.cluster import KMeans

X = np.array([
    [1000, 2],
    [1200, 3],
    [1100, 2],
    [5000, 10],
    [5200, 11],
    [4800, 9]
])

model = KMeans(n_clusters=2, random_state=1, n_init=10)
model.fit(X)

new_customer = [[1500, 3]]
cluster = model.predict(new_customer)
print("Customer belongs to cluster:", cluster[0])
