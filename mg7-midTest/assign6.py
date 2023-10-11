from assign3 import train_data

def minmax(data):
    min = 0
    max = 1
    minval = data.min()
    maxval = data.max()
    data = (data - minval) * (max - min) / (maxval - minval) + min
    return data


minPclass = train_data['Pclass'].min()
maxPclass = train_data['Pclass'].max()
minFare = train_data['Fare'].min()
maxFare = train_data['Fare'].max()

dataPclass = train_data['Pclass']
dataFare = train_data['Fare']

train_data['Pclass'] = minmax(dataPclass)
train_data['Fare'] = minmax(dataFare)

# print(train_data)
