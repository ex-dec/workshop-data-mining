from assign1 import dataset

transaksi = dataset.groupby(['Country', 'InvoiceNo'])['Qty'].mean().reset_index()
# print(transaksi)
