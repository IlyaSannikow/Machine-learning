import numpy as np

arr = np.zeros((5,5))

for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if i%2==0 and j%2!=0:
            arr[i][j] = 1
        elif i%2!=0 and j%2==0:
            arr[i][j] = 1

print(arr)