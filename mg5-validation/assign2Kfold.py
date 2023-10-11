from assign1 import dataset

row = len(dataset)
part = 10
part_range = row/part

for i in range(part):
    first_index_test = int(row/part*i)
    last_index_test = int(first_index_test+part_range)
    test_data = dataset.iloc[first_index_test:last_index_test]
    train_data = dataset.drop(test_data.index)
