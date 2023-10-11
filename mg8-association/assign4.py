from assign3 import transaksi
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


frequent_itemsets=apriori(transaksi, min_support=0.2, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print("\nAssociation Rules: \n", rules[['antecedents', 'consequents', 'confidence']])