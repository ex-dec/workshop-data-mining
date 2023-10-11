import pandas as pd

dataset = pd.read_csv("titanic.csv")
featureData = pd.DataFrame(dataset, columns=['Age', 'Fare'])
print(featureData)