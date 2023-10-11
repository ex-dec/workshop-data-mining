from assign2 import data

transaksi = data.groupby(['InvoiceNo','StockCode'])['Qty'].sum()
transaksi = transaksi.unstack().reset_index().fillna(0).set_index('InvoiceNo')
transaksi[transaksi>0] = 1

# print(transaksi)