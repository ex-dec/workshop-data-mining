import pandas as pd
from assign1 import dataset

train_data = pd.DataFrame(dataset[['Sex', 'Age', 'Pclass', 'Fare']])
train_data = train_data.fillna(train_data.loc[:, 'Age'].mean())
print(train_data)
