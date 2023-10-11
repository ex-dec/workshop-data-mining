import pandas as pd

dataset = pd.read_csv('ruspini_missing.csv')
print('Dataset', dataset)
dataset = dataset.fillna(dataset.groupby('CLASS').transform('mean'))
print('\n\nDataset setelah pengisian missing value\n', dataset)
