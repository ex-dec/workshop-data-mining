from assign6 import train_data
from assign4 import train_label
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

label_encoder = LabelEncoder()
train_label_encoded = label_encoder.fit_transform(train_label)

train_data[train_data.columns[0]] = LabelEncoder().fit_transform(train_data['Sex'])

kNN = KNeighborsClassifier(n_neighbors=3, weights='distance')
kNN.fit(train_data, train_label_encoded)

class_result = kNN.predict(train_data)

class_result = label_encoder.inverse_transform(class_result)

print(class_result)
