import numpy as np

arr = np.full((4, 4), 7)

for i in range(0,len(arr)):
    arr[i][i] = i+1

print(arr)