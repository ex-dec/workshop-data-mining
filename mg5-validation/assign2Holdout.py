from assign1 import dataset

row = len(dataset)

train_size = 0.7
num_train_row = int(row * train_size)

train_data = dataset.iloc[0:num_train_row]
test_data = dataset.iloc[num_train_row:row]
