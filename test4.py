# from sklearn.cluster import KMeans
# import numpy as np
# X = np.array([[1, 2], [1, 4], [1, 0],
#               [10, 2], [10, 4], [10, 0],[5, 5],[1, 3]])
# kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
# print(kmeans.labels_)

from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0],
              [5, 5], [1, 3]])

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)

labels = kmeans.labels_

# Custom names
custom_names = {0: "c1", 1: "c2"}

custom_labels = [custom_names[i] for i in labels]

print("Original:", labels)
print("Custom:", custom_labels)