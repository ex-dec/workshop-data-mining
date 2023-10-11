import pandas as pd
from assign4 import pos_missing_test

testlabel_dataset = pd.read_csv('titanic_testlabel.csv')
testlabel_dataset = testlabel_dataset.loc[:, ['Survived']]
test_label = testlabel_dataset.loc[~testlabel_dataset.index.isin(pos_missing_test)]
# print(test_label)
