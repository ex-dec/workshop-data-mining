from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def knn(train_data, train_labels, test_data, test_labels):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_data, train_labels)
    predictions = knn.predict(test_data)
    error_ratio = 1 - accuracy_score(test_labels, predictions)
    return error_ratio