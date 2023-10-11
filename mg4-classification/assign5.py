import pandas as pd

dataset = pd.read_csv('titanic.csv')

train_data = dataset[['Age', 'Fare']].copy()
pos_missing_train = train_data[train_data.isnull().any(axis=1)].index.tolist()
train_label = dataset.loc[~dataset.index.isin(pos_missing_train), 'Survived']

# print(train_label)
