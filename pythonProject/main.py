import pandas as pd

dataset = pd.read_csv('Aceh.csv')
datasetFrame = pd.DataFrame(dataset)
print(datasetFrame.columns)