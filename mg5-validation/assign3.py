import pandas as pd

def fill_age(data):
    data= data[["Sex", "Age", "Pclass", "Fare"]]

    data_copy = data.copy()
    data_copy.loc[data_copy["Age"].isnull(), "Age"] = data_copy.groupby("Pclass")["Age"].transform("mean")

    return data_copy