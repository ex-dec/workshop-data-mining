from assign2 import test_dataset
import pandas as pd

test_data = pd.DataFrame(test_dataset[['Sex', 'Age', 'Pclass', 'Fare']])
test_data.dropna(inplace=True)
# print(test_data)