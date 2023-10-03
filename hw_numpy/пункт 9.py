import numpy as np

arr = np.zeros((5,5))

for i in range(0,len(arr)):
    j = 0
    while j < len(arr):
        arr[i][j] = i
        j +=1

print(arr)