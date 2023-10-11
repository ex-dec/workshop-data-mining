import pandas as pd


def minmax(data):
    min = 0
    max = 1
    minval = data.min()
    maxval = data.max()
    data = (data - minval) * (max - min) / (maxval - minval) + min
    return data


dataset = pd.read_csv('titanic.csv')

train_data = dataset[['Age', 'Fare']].copy()
pos_missing_train = train_data[train_data.isnull().any(axis=1)].index.tolist()
train_data.dropna(inplace=True)
train_label = dataset.loc[~dataset.index.isin(pos_missing_train), 'Survived']

dataAge = train_data['Age']
dataFare = train_data['Fare']
datasetFrame = pd.DataFrame(train_data)

minAge = train_data['Age'].min()
maxAge = train_data['Age'].max()
minFare = train_data['Fare'].min()
maxFare = train_data['Fare'].max()

train_data['Age'] = minmax(dataAge)
train_data['Fare'] = minmax(dataFare)

# print(train_data)