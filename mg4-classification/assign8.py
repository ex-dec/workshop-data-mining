import pandas as pd
from assign7 import minAge
from assign7 import maxAge
from assign7 import minFare
from assign7 import maxFare
from assign4 import test_data


def minmax_test(data, minval, maxval):
    min = 0
    max = 1
    data = (data - minval) * (max - min) / (maxval - minval) + min
    return data


dataAge = test_data['Age']
dataFare = test_data['Fare']
datasetFrame = pd.DataFrame(test_data)

test_data['Age'] = minmax_test(dataAge, minAge, maxAge)
test_data['Fare'] = minmax_test(dataFare, minFare, maxFare)

# print(test_data)
