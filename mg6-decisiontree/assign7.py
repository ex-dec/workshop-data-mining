import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


from assign3 import train_data
from assign5 import train_label
from assign4 import test_data

train_data[train_data.columns[0]] = LabelEncoder().fit_transform(train_data['Sex'])
test_data[test_data.columns[0]] = LabelEncoder().fit_transform(test_data['Sex'])

dtc = DecisionTreeClassifier()
dtc.fit(train_data,train_label)
class_result = dtc.predict(test_data)
print('Class = \n', class_result)

acc = dtc.score(train_data, train_label)
err = round((1-acc)*100,2)
print("\n\n Error ratio = ", err, '%')