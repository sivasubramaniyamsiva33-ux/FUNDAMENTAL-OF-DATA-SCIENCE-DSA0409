"""
Exercise 35: K-Means Clustering for Retail Customers
Key Idea: segment retail shoppers into three distinct behavior clusters and view centroids.
"""

import pandas as pd
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Spending": [500, 700, 600, 4000, 4500, 4200, 1500, 1700],
    "Visits": [2, 3, 2, 10, 12, 11, 5, 6]
})

model = KMeans(n_clusters=3, random_state=1, n_init=10)
data["Cluster"] = model.fit_predict(
    data[["Spending", "Visits"]]
)

print(data)
print("Cluster centers:")
print(model.cluster_centers_)
