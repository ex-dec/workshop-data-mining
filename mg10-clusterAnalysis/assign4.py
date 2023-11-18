from assign3 import transaksi
from sklearn.cluster import KMeans

cluster = transaksi[['Qty']]

cluster_i = []
cluster_val = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=3, random_state=0)
    clusters = kmeans.fit_predict(cluster)
    cluster_i.append(i)
    cluster_val.append(kmeans.inertia_)
#     print(f"Cluster {i}:\n", clusters)
#
# for i in range(10):
#     print(f"Cluster {cluster_i[i]} - SSE: {cluster_val[i]}")
