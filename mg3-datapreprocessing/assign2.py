import pandas as pd

dataset = pd.read_csv('titanic.csv')
rows, cols = dataset.shape
print('Jumlah baris = ', rows)
print('Jumlah kolom = ', cols)
