from assign1 import dataset

row = len(dataset)
part = 10
part_range = row/part

for i in range(row):
    test_data = dataset.iloc[i]
    train_data = dataset.drop(i)
