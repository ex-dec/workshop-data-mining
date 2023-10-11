from assign1 import dataset
import pandas as pd

data = pd.DataFrame(dataset[['Sex', 'Age', 'Pclass', 'Fare', 'Survived']])

pos_missing_train = data[data.isnull().any(axis=1)].index.tolist()

# print(data)