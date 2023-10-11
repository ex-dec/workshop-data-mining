import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


dataset = pd.read_csv("pembelian.csv")
transaksi = dataset.groupby(['No_Kwitansi','Nama_Barang'])['Jumlah'].sum()

transaksi = transaksi.unstack().reset_index().fillna(0).set_index('No_Kwitansi')
transaksi[transaksi>0] = 1
print('Tabel Transaksi \n', transaksi)

# frequent_itemsets=apriori(transaksi, min_support=0.3, use_colnames=True)
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# print("\nAssociation Rules: \n", rules[['antecedents', 'consequents', 'confidence']])