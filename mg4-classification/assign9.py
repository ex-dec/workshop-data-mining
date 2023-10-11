from sklearn.neighbors import KNeighborsClassifier
from assign8 import test_data
from assign7 import train_data
from assign5 import train_label

kNN = KNeighborsClassifier(n_neighbors=1, weights='distance')
kNN = KNeighborsClassifier(n_neighbors=2, weights='distance')
kNN = KNeighborsClassifier(n_neighbors=3, weights='distance')
kNN = KNeighborsClassifier(n_neighbors=4, weights='distance')
kNN = KNeighborsClassifier(n_neighbors=5, weights='distance')
kNN = KNeighborsClassifier(n_neighbors=6, weights='distance')
kNN.fit(train_data, train_label)

class_result = kNN.predict(test_data)

print(class_result)