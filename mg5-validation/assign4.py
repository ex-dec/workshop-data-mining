import pandas as pd
from assign1 import dataset

label = pd.DataFrame(dataset[['Survived']])
print(label)