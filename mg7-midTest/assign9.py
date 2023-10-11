from assign8 import class_result
from assign2 import pos_missing_train
from assign2 import data

j = 0
for i in pos_missing_train:
    data['Age'][i] = class_result[j]
    j+=1

print(data)