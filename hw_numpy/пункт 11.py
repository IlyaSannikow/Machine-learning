import numpy as np

arr = np.random.randint(0, 10, (10, 10)) # случайные от 0 до 10, размера (10 на 10)

print(arr,'\n'*2)

for i in range(0,len(arr)):
    center_row = (max(arr[i]) + min(arr[i]))/2
    for j in range(0,len(arr)):
        arr[i][j] -= center_row

print(arr)