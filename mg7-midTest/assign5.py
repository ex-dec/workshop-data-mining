from assign2 import data
from assign2 import pos_missing_train
import pandas as pd

test_data = pd.DataFrame(data[['Sex', 'Pclass', 'Fare', 'Survived']])
test_data = test_data.iloc[pos_missing_train]

# print(test_data)
