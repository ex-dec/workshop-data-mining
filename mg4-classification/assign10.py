import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from assign8 import test_data
from assign7 import train_data
from assign5 import train_label
from assign6 import test_label

kNN = KNeighborsClassifier(n_neighbors=1, weights='distance')
kNN.fit(train_data, train_label)
class_result = kNN.predict(train_data)
class_result = pd.DataFrame(class_result, columns=['Survived'])

print(class_result)

# precission_ratio = kNN.score(class_result, test_label)
# error_ratio = 1 - precission_ratio

# print(precission_ratio)
# print(error_ratio)