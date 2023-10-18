from assign6 import sorted_centroids
from assign4 import transaksi

# Menentukan cluster transaksi rendah, sedang, dan tinggi
centroid_values = list(sorted_centroids.values())
low_transaction_cluster = list(sorted_centroids.keys())[0]
medium_transaction_cluster = list(sorted_centroids.keys())[1]
high_transaction_cluster = list(sorted_centroids.keys())[2]

# Menampilkan negara-negara dalam setiap cluster
transaksi_rendah = transaksi[transaksi['Cluster'] == int(low_transaction_cluster[-1])]
transaksi_sedang = transaksi[transaksi['Cluster'] == int(medium_transaction_cluster[-1])]
transaksi_tinggi = transaksi[transaksi['Cluster'] == int(high_transaction_cluster[-1])]

print("Cluster Transaksi Rendah:", transaksi_rendah['Country'].tolist())
print("Cluster Transaksi Sedang:", transaksi_sedang['Country'].tolist())
print("Cluster Transaksi Tinggi:", transaksi_tinggi['Country'].tolist())