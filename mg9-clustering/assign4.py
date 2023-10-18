from assign3 import transaksi
from sklearn.cluster import AgglomerativeClustering

data = transaksi.values.reshape(-1, 1)

clustering = AgglomerativeClustering(n_clusters=3, linkage='average')

clusters = clustering.fit_predict(data)

transaksi = transaksi.reset_index()
transaksi['Cluster'] = clusters

# print(clusters)