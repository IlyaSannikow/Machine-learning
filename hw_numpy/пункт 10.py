import numpy as np

arr = np.random.randint(0, 9, (10, 10)) # от 0 до 9, размера (10 на 10)
aver_column = np.mean(arr,axis=1)

print(arr, '\n'*2, aver_column, '\n'*2)

for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        arr[i][j] -= aver_column[i]

print(arr)