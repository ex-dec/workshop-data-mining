import pandas as pd

def zscore(data):
    meanval = data.mean()
    stdval = data.std()
    data = (data - meanval) / stdval
    return data

dataset = pd.read_csv("titanic.csv")
dataAge = dataset['Age']
dataFare = dataset['Fare']
datasetFrame = pd.DataFrame(dataset)
datasetFrame['Age'] = datasetFrame['Age'].fillna(datasetFrame.groupby('Survived')['Age'].transform('mean'))

dataset['Age'] = zscore(dataAge)
dataset['Fare'] = zscore(dataFare)

print(dataset[['Age', 'Fare']])