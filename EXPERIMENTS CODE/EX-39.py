"""
Exercise 39: K-Means Clustering and Visualization
Key Idea: cluster customers on spending and item count, visualizing cluster distribution.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Spending": [500, 600, 550, 3000, 3200, 3100, 1500, 1600],
    "Items": [2, 3, 2, 10, 11, 9, 5, 6]
})

model = KMeans(n_clusters=3, random_state=1, n_init=10)
data["Cluster"] = model.fit_predict(
    data[["Spending", "Items"]]
)

print(data)

plt.scatter(
    data["Spending"],
    data["Items"],
    c=data["Cluster"]
)
plt.xlabel("Total Spending")
plt.ylabel("Number of Items")
plt.title("Customer Segments")
plt.show()
