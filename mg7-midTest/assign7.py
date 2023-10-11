from assign6 import minPclass
from assign6 import minFare
from assign6 import maxPclass
from assign6 import maxFare
from assign5 import test_data


def minmax_test(data, minval, maxval):
    min = 0
    max = 1
    data = (data - minval) * (max - min) / (maxval - minval) + min
    return data

dataPclass = test_data['Pclass']
dataFare = test_data['Fare']

test_data['Pclass'] = minmax_test(dataPclass, minPclass, maxPclass)
test_data['Fare'] = minmax_test(dataFare, minFare, maxFare)

# print(test_data)