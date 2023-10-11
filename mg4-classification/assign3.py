import pandas as pd

dataset = pd.read_csv('titanic.csv')

train_data = dataset[['Age', 'Fare']].copy()
pos_missing_train = train_data[train_data.isnull().any(axis=1)].index.tolist()
train_data.dropna(inplace=True)

# print(pos_missing_train)
# print(train_data)
