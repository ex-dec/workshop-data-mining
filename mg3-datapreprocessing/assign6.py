import pandas as pd
def minmax(data):
    min = 0
    max = 1
    minval = data.min()
    maxval = data.max()
    data = (data - minval) * (max - min) / (maxval - minval) + min
    return data

dataset = pd.read_csv("titanic.csv")
dataAge = dataset['Age']
dataFare = dataset['Fare']
datasetFrame = pd.DataFrame(dataset)
datasetFrame['Age'] = datasetFrame['Age'].fillna(datasetFrame.groupby('Survived')['Age'].transform('mean'))

dataset['Age'] = minmax(dataAge)

dataset['Fare'] = minmax(dataFare)

print(dataset[['Age', 'Fare']])