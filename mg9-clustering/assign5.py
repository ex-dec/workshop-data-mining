from assign4 import clusters
from assign4 import data
import numpy as np

centroids = {}
for cluster_id in range(3):
    cluster_data = data[clusters == cluster_id]
    centroid = np.mean(cluster_data)
    centroids[f'Cluster {cluster_id + 1}'] = centroid

# print(centroids)