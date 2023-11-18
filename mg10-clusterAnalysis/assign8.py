from assign1 import dataset
from sklearn.cluster import KMeans

cluster = dataset[['Qty']]

kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(cluster)

centroid_positions = kmeans.cluster_centers_

sorted_centroid_positions = sorted(centroid_positions)

low_cluster = sorted_centroid_positions[0]
medium_cluster = sorted_centroid_positions[1]
high_cluster = sorted_centroid_positions[2]

low_country = dataset[clusters == 0]['Country']
medium_country = dataset[clusters == 1]['Country']
high_country = dataset[clusters == 2]['Country']

print("Cluster Transaksi Rendah (Indeks 0):")
print(low_country.unique())

print("\nCluster Transaksi Sedang (Indeks 1):")
print(medium_country.unique())

print("\nCluster Transaksi Tinggi (Indeks 2):")
print(high_country.unique())
