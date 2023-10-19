from assign1 import dataset
from assign3 import fill_age
from assign4 import take_label
from assign5and6 import minmax_train
from assign7 import knn
from labelEncoder import label_encoder

train_size = 0.7

row = len(dataset)

num_train_row = int(row * train_size)

train_data = dataset.iloc[:num_train_row]
test_data = dataset.iloc[num_train_row:]

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
print("Error ratio : ", error)
