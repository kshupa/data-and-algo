from array import Array
import random

valueList = Array(100)

for i in range(len(valueList)):
    valueList[i] = random.random()

print(valueList)
