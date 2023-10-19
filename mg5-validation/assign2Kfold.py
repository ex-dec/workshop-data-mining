from assign1 import dataset
from assign3 import fill_age
from assign4 import take_label
from assign5and6 import minmax_train
from assign7 import knn
from labelEncoder import label_encoder
from sklearn.model_selection import KFold

kf = KFold(n_splits=10)
fold_index = 1
error_ratio = 0

for train_index, test_index in kf.split(dataset):
    train_data = dataset.iloc[train_index]
    test_data = dataset.iloc[test_index]
    fold_index += 1

    # print("Train Data \n", train_data)
    # print("Test Data \n", test_data)

    train_labels = take_label(train_data)
    test_labels = take_label(test_data)

    # print("Train Label \n", train_labels)

    train_data = fill_age(train_data)
    test_data = fill_age(test_data)

    # print("Train Data \n", train_data)
    # print("Test Data \n", test_data)


    minmax_train(train_data, test_data)

    # print("Train Data \n", train_data)
    # print("Test Data \n", test_data)

    label_encoder(train_data, test_data)

    error = knn(train_data, train_labels, test_data, test_labels)
    error_ratio += error

fold_index -= 1
error_ratio = error_ratio / fold_index
print("Error ratio : ", error_ratio)