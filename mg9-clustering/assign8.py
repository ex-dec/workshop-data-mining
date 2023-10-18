import matplotlib.pyplot as plt
from assign7 import transaksi
from assign5 import clusters

# Visualisasi hasil cluster
plt.figure(figsize=(10, 6))
plt.scatter(range(len(transaksi)), transaksi['InvoiceNo'], c=clusters, cmap='rainbow')
plt.xlabel('Urutan Country')
plt.ylabel('Jumlah Transaksi')
plt.title('Clustering Hasil Transaksi')
plt.xticks(range(len(transaksi)), transaksi['Country'], rotation=90)
plt.colorbar(label='Cluster')
plt.show()