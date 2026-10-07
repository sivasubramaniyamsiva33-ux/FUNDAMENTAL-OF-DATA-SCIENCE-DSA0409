"""
Exercise 31: Customer Segmentation using K-Means
Key Idea: segment customer behavior based on spending and visit counts using K-Means clustering.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Spending": [1000, 1200, 1100, 5000, 5200, 4800],
    "Visits": [2, 3, 2, 10, 11, 9]
})

model = KMeans(n_clusters=2, random_state=1, n_init=10)
data["Cluster"] = model.fit_predict(
    data[["Spending", "Visits"]]
)

print(data)

plt.scatter(
    data["Spending"],
    data["Visits"],
    c=data["Cluster"]
)
plt.xlabel("Spending")
plt.ylabel("Visits")
plt.title("Customer Segmentation")
plt.show()
