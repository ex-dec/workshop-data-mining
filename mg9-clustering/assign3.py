from assign2 import dataset

transaksi = dataset.groupby('Country')['InvoiceNo'].nunique()
# print(transaksi)