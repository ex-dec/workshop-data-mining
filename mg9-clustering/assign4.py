from assign3 import transaksi
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt

data = transaksi.values.reshape(-1, 1)

clustering = AgglomerativeClustering(n_clusters=3, linkage='average')

clusters = clustering.fit_predict(data)

transaksi = transaksi.reset_index()
transaksi['Cluster'] = clusters

centroids = {}
for cluster_id in range(3):
    cluster_data = data[clusters == cluster_id]
    centroid = np.mean(cluster_data)
    centroids[f'Cluster {cluster_id + 1}'] = centroid

sorted_centroids = dict(sorted(centroids.items(), key=lambda item: item[1]))

# Menentukan cluster transaksi rendah, sedang, dan tinggi
centroid_values = list(sorted_centroids.values())
low_transaction_cluster = list(sorted_centroids.keys())[0]
medium_transaction_cluster = list(sorted_centroids.keys())[1]
high_transaction_cluster = list(sorted_centroids.keys())[2]

# Menampilkan negara-negara dalam setiap cluster
low_transaction_countries = transaksi[transaksi['Cluster'] == int(low_transaction_cluster[-1])]
medium_transaction_countries = transaksi[transaksi['Cluster'] == int(medium_transaction_cluster[-1])]
high_transaction_countries = transaksi[transaksi['Cluster'] == int(high_transaction_cluster[-1])]

# print("Cluster Transaksi Rendah:", low_transaction_countries['Country'].tolist())
# print("Cluster Transaksi Sedang:", medium_transaction_countries['Country'].tolist())
# print("Cluster Transaksi Tinggi:", high_transaction_countries['Country'].tolist())
#
