import pandas as pd
import numpy as np

def zscore(data):
    meanval = data.mean()
    stdval = data.std()
    data = (data - meanval) / stdval
    return data

def sigmoidal(data):
    data = (1-np.exp(-zscore(data))) / (1+np.exp(-zscore(data)))
    return data

dataset = pd.read_csv("titanic.csv")
dataAge = dataset['Age']
dataFare = dataset['Fare']
datasetFrame = pd.DataFrame(dataset)
datasetFrame['Age'] = datasetFrame['Age'].fillna(datasetFrame.groupby('Survived')['Age'].transform('mean'))

dataset['Age'] = sigmoidal(dataAge)
dataset['Fare'] = sigmoidal(dataFare)

print(dataset[['Age', 'Fare']])