import pandas as pd

dataset = pd.read_csv("titanic.csv")
classData = pd.DataFrame(dataset, columns=['Survived'])
print(classData)