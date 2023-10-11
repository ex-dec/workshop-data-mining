from assign2 import data
from assign2 import pos_missing_train
import pandas as pd

train_data = pd.DataFrame(data[['Sex', 'Pclass', 'Fare', 'Survived']])
train_data = train_data.loc[~train_data.index.isin(pos_missing_train)]

# print(train_data)