import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Membaca file CSV
dataset = pd.read_csv("transaction.csv")

# Pilih kolom yang akan digunakan untuk clustering, misalnya 'Qty'
data_for_clustering = dataset[['Qty']]

# Melakukan clustering dengan K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(data_for_clustering)

# Menambahkan kolom 'Cluster' ke dataset
dataset['Cluster'] = clusters

# Mendapatkan posisi centroid dari setiap cluster
centroid_positions = kmeans.cluster_centers_

# Mengurutkan posisi centroid secara ascending
sorted_centroid_positions = sorted(centroid_positions)

# Membuat plot dengan negara di sumbu x
plt.figure(figsize=(12, 6))
colors = ['red', 'green', 'blue']

for i, color in zip(range(3), colors):
    cluster_data = dataset[dataset['Cluster'] == i]
    plt.scatter(cluster_data['Country'], cluster_data['Qty'], c=color, label=f'Cluster {i + 1}')

plt.xlabel('Negara')
plt.ylabel('Transaksi')
plt.legend()
plt.title('Hasil Clustering dengan Warna yang Berbeda Menurut Negara')
plt.xticks(rotation=90)
plt.show()
