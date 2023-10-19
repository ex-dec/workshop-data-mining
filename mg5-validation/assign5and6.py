import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def minmax_train(train_data, test_data):
    scaler = MinMaxScaler()

    columns_to_normalize = ["Age", "Fare"]

    train_data[columns_to_normalize] = scaler.fit_transform(train_data[columns_to_normalize])
    test_data[columns_to_normalize] = scaler.transform(test_data[columns_to_normalize])