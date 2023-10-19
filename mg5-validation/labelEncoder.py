from sklearn.preprocessing import LabelEncoder

def label_encoder(train_data, test_data):
    label_encoder = LabelEncoder()

    train_data["Sex"] = label_encoder.fit_transform(train_data["Sex"])
    test_data["Sex"] = label_encoder.transform(test_data["Sex"])

