from assign2 import data
from assign2 import pos_missing_train
import pandas as pd

train_label = pd.DataFrame(data[['Age']])
train_label = train_label.loc[~train_label.index.isin(pos_missing_train)]

# print(train_label)