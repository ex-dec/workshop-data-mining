import pandas as pd

test_dataset = pd.read_csv('titanic_test.csv')

test_data = test_dataset[['Age', 'Fare']].copy()
pos_missing_test = test_data[test_data.isnull().any(axis=1)].index.tolist()
test_data.dropna(inplace=True)

# print(pos_missing_test)
# print(test_data)
