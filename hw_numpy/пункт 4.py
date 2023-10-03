import numpy as np

arr = []

for i in range(10,100):
    if i%2 ==0:
        arr.append(i)

vec = np.array(arr)

print(vec)