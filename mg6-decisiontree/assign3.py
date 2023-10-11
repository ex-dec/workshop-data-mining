from assign1 import dataset
import pandas as pd

train_data = pd.DataFrame(dataset[['Sex', 'Age', 'Pclass', 'Fare']])
train_data.fillna({
    'Age': train_data["Age"].mean(),
    'Pclass': train_data["Pclass"].mean(),
    'Fare': train_data["Fare"].mean()},
    inplace=True
)
# print(train_data)