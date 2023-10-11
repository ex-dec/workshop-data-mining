import pandas as pd

dataset = pd.read_csv('ruspini.csv')
dataX = dataset['X']

minval = dataX.min()
maxval = dataX.max()
avgval = dataX.mean()
stdval = dataX.std()

print('Nilai minimum = ', minval)
print('Nilai maksimum = ', maxval)
print('Nilai rata-rata = ', avgval)
print('Nilai standar deviasi = ', stdval)
