import pandas as pd

dataset = pd.read_csv("titanic.csv")
datasetFrame = pd.DataFrame(dataset)
datasetFrame['Age'] = datasetFrame['Age'].fillna(datasetFrame.groupby('Survived')['Age'].transform('mean'))
print(datasetFrame[["Age"]])